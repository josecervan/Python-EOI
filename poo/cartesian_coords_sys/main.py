from cartesian_models import Point, Rectangle


A = Point(x=2, y=3)
B = Point(x=-5, y=5)
C = Point(x=-3, y=-1)
D = Point(x=4, y=-7)
E = Point(x=0, y=-9)
F = Point(x=7, y=0)
G = Point()

r = Rectangle(init=A, final=B)

print('--')
print(f'A{A}: {A.quadrant()}')
print(f'B{B}: {B.quadrant()}')
print(f'C{C}: {C.quadrant()}')
print(f'D{D}: {D.quadrant()}')
print(f'E{E}: {E.quadrant()}')
print(f'F{F}: {F.quadrant()}')
print(f'G{G}: {G.quadrant()}')
print('--')
print(f'AB = {B.vector(A)}')
print(f'BA = {A.vector(B)}')
print('--')
print(f'dist(A,B) = {A.distance(B)}')
print(f'dist(B,A) = {B.distance(A)}')
print('--')
print(f'Farthest from (0,0) in (A,B,C): {max([A, B, C], key=lambda p: p.distance(Point()))}')
print('--')
print(f'Rectangle: init{r.init}, final{r.final}')
print(f'Base = {r.base()}')
print(f'Height: {r.height()}')
print(f'Area = {r.area()}')
print('--')