#https://scipython.com/blog/penrose-tiling-2/
from math import pi, cos, sin

from tiles.tile import RhombusTile,PentacleTile
from tiles.utils import golden_ratio, inverse_golden_ratio


#############
scale = 100
angle = pi / 5
rotation2 = cos(angle*2) + 1j*sin(angle*2)

A = -scale/2 + 0j
B = scale/2 * rotation2
C = scale/2 / golden_ratio + 0j

seed_rhombus = [RhombusTile(A, B, C)]
#############


rotation = cos(angle) + 1j*sin(angle)
A1 = scale + 0.j
B = 0 + 0j
C1 = C2 = A1 * rotation
A2 = A3 = C1 * rotation
C3 = C4 = A3 * rotation
A4 = A5 = C4 * rotation
C5 = -A1
seed_circle = [
    PentacleTile(A1, B, C1), 
    PentacleTile(A2, B, C2),
    PentacleTile(A3, B, C3), 
    PentacleTile(A4, B, C4),
    PentacleTile(A5, B, C5)
]
#############


P = scale * rotation2
Q = P*rotation2
C = -scale * (1/golden_ratio)
R = C / rotation2
S = R / rotation2

seed_star = [
    RhombusTile(0,scale,S),
    RhombusTile(0,P,S),
    RhombusTile(0,P,R),
    RhombusTile(0,Q,R),
    RhombusTile(0,Q,C)    
]
#############