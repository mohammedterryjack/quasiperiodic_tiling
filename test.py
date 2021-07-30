from example_seed_tiles import seed_star,seed_rhombus,seed_circle
from tiles.tesselate import Tesselate 

tiling = Tesselate(seed_tiles=seed_rhombus)
tiling.generate()
tiling.write_svg('rhombus.svg')

tiling = Tesselate(seed_tiles=seed_circle,iterations=6)
tiling.generate()
tiling.write_svg('circle.svg')

tiling = Tesselate(seed_tiles=seed_star,scale=150,iterations=6)
tiling.generate()
tiling.write_svg('star.svg')