from typing import Tuple

from tiles.penrose_tile import RobinsonTriangle
from tiles.utils import inverse_golden_ratio,golden_ratio

class RhombusTile(RobinsonTriangle):
    def inflate(self) -> Tuple["RhombusTile","PentacleTile","RhombusTile"]:
        D = inverse_golden_ratio * self.A + golden_ratio * self.C
        E = inverse_golden_ratio * self.A + golden_ratio * self.B
        return (
            RhombusTile(D, E, self.A),
            PentacleTile(E, D, self.B),
            RhombusTile(self.C, D, self.B)
        )

class PentacleTile(RobinsonTriangle):
    def inflate(self) -> Tuple["PentacleTile","RhombusTile"]:
        D = golden_ratio * self.A + inverse_golden_ratio * self.B
        return (
            PentacleTile(D, self.C, self.A),
            RhombusTile(self.C, D, self.B)
        )
