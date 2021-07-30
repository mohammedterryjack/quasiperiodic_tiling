from typing import Tuple

from tiles.utils import cross

class RobinsonTriangle:
    def __init__(self, vertex_a:complex,vertex_b:complex,vertex_c:complex) -> None:
        self.A = vertex_a
        self.B = vertex_b
        self.C = vertex_c

    def rhombus_centre(self) -> float:
        return (self.A + self.C) / 2
    
    def rhombus_path(self,rhombus:bool=True) -> str:
        AB = self.B - self.A
        BC = self.C - self.B
        if rhombus:
            return f"m{self.A.real},{self.A.imag}, l{AB.real},{AB.imag} l{BC.real},{BC.imag} l{-AB.real},{-AB.imag}z"
        return f"m{self.A.real},{self.A.imag} l{AB.real},{AB.imag} l{BC.real},{BC.imag}z"

    def flip(self) -> "RobinsonTriangle":
        return self.__class__(
            vertex_a = self.A.conjugate(), 
            vertex_b = self.B.conjugate(),
            vertex_c = self.C.conjugate()
        )