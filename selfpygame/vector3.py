from functools import singledispatch
import typing

# ? operators: https://yumarublog.com/python/operator/


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z
            )
        raise TypeError('Type is not Vector3.')

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z
            )
        raise TypeError('Type is not Vector3.')

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z
            )
        elif isinstance(other, (float, int)):
            return Vector3(
                self.x * other,
                self.y * other,
                self.z * other
            )
        raise TypeError('Type is not Vector3.')

    # def string(self):
    #     return f'({self.x},{self.y},{self.z})'

    def __str__(self) -> str:
        return f'({self.x},{self.y},{self.z})'


if __name__ == '__main__':
    v1 = Vector3(2, 4, 6)
    v2 = Vector3(3, 5, 7)

#     print(f'v1: {v1.string()}\nv2: {v2.string()}\n\
# ----------------\n\
# +: {(v1 + v2).string()}\n-: {(v1 - v2).string()}\n\
# *: {(v1 * v2).string()}\n*: {(v1 * 2).string()}')
    print(f'v1: {v1}\nv2: {v2}\n\
----------------\n\
+: {(v1 + v2)}\n-: {(v1 - v2)}\n\
*: {(v1 * v2)}\n*: {(v1 * 2)}')

'''
[Running] python -u "d:\desktop\selfpygame\vector3.py"
v1: (2,4,6)
v2: (3,5,7)
----------------
+: (5,9,13)
-: (-1,-1,-1)
*: (6,20,42)
*: (4,8,12)

[Done] exited with code=0 in 0.097 seconds
'''
