from typing import List, Optional
from random import randint 
from math import cos, sin

from tiles.penrose_tile import RobinsonTriangle
from tiles.utils import inverse_golden_ratio

class Tesselate:
    def __init__(
        self,
        seed_tiles:Optional[List[RobinsonTriangle]] = None,
        scale:int=100,
        iterations:int=5,
        rotation:int=0,
        reflection:bool=True,
        horizontal_flip:bool=False,
        vertical_flip:bool=False,
        draw_rhombus:bool=True,
        stroke_colour:str='#fff',
        base_stroke_width:float=.05,
        tile_opacity:float=.6,
        margin:float=1.05        
    ) -> None:
        self.scale = scale
        self.iterations = iterations
        self.rotation = rotation
        self.reflection = reflection
        self.horizontal_flip = horizontal_flip
        self.vertical_flip = vertical_flip
        self.draw_rhombus = draw_rhombus
        self.stroke_colour = stroke_colour
        self.base_stroke_width = base_stroke_width
        self.tile_opacity = tile_opacity
        self.margin = margin
        if seed_tiles is None:
            self.tiles = []
        else:
            self.tiles = seed_tiles

    def remove_duplicates(self,minimum_delta:float=1.e-5) -> None:
        sorted_tiles = sorted(self.tiles, key=lambda tile: (tile.rhombus_centre().real, tile.rhombus_centre().imag))
        self.tiles = [sorted_tiles[0]]
        for index, tile in enumerate(sorted_tiles[1:], start=1):
            neighbour_tile = sorted_tiles[index-1]
            if abs(tile.rhombus_centre() - neighbour_tile.rhombus_centre()) > minimum_delta:
                self.tiles.append(tile)

    def inflate(self) -> None:
        new_tiles = []
        for tile in self.tiles:
            new_tiles.extend(tile.inflate())
        self.tiles = new_tiles

    def rotate(self) -> None:
        angle = cos(self.rotation) + 1j * sin(self.rotation)
        for tile in self.tiles:
            tile.A *= angle
            tile.B *= angle
            tile.C *= angle

    def reflect(self) -> None:
        self.tiles.extend(
            [
                tile.flip() for tile in self.tiles
            ]
        )

    def flip_y(self) -> None:
        for tile in self.tiles:
            tile.A = complex(-tile.A.real, tile.A.imag)
            tile.B = complex(-tile.B.real, tile.B.imag)
            tile.C = complex(-tile.C.real, tile.C.imag)

    def flip_x(self) -> None:
        for tile in self.elements:
            tile.A = tile.A.flip()
            tile.B = tile.B.flip()
            tile.C = tile.C.flip()

    def generate(self) -> None:
        for _ in range(self.iterations):
            self.inflate()
        
        if self.draw_rhombus:
            self.remove_duplicates()

        if self.reflection:
            self.reflect()
            self.remove_duplicates()
        
        if self.rotation:
            self.rotate()

        if self.vertical_flip:
            self.flip_y()

        if self.horizontal_flip:
            self.flip_x()

    def make_svg(self) -> str:
        xmin = ymin = -self.scale * self.margin
        xmax = ymax = 2*self.scale * self.margin
        stroke_width = inverse_golden_ratio**self.iterations * self.scale * self.base_stroke_width
        tile_pattern = '\n'.join(
            f'<path fill="{self.random_tile_colour()}" fill-opacity="{self.tile_opacity}" d="{tile.rhombus_path(self.draw_rhombus)}"/>' for tile in self.tiles
        )
        svg_header = '<?xml version="1.0" encoding="utf-8"?>'
        svg_style = f'width="100%" height="100%" viewBox="{xmin} {ymin} {xmax} {ymax}" preserveAspectRatio="xMidYMid meet" version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg"'
        g_style = f'style="stroke:{self.stroke_colour}; stroke-width: {stroke_width}; stroke-linejoin: round;"'
        return f"""{svg_header}
<svg {svg_style}>
<g {g_style}>
{tile_pattern}
</g>
</svg>
"""

    def write_svg(self, filename:str) -> None:
        with open(filename, 'w') as svg_file:
            svg_file.write(self.make_svg())

    @staticmethod
    def random_tile_colour() -> str:
        return '#' + hex(randint(0,0xfff))[2:]