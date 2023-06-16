from functools import singledispatch
from vector3 import Vector3
from mathf import Mathf
import numpy


class OL:
    # overload
    @singledispatch
    def computer(n1: int, n2: int):
        return n1 + n2

    @computer.register
    def _computer(n1: float, n2: float):
        return n1 * n2


if __name__ == '__main__':
    v1 = Vector3(2, 4, 6)
    v2 = Vector3(3, 5, 7)

#     print(f'v1: {v1}\nv2: {v2}\n\
# ----------------\n\
# +: {(v1 + v2)}\n-: {(v1 - v2)}\n\
# *: {(v1 * v2)}\n*: {(v1 * 2)}')

    # print(Vector3.distance(v1, v2))

    # print(Mathf.round(Vector3.distance(v1, v2), 1))

    print(Mathf.lerp(0, 1, 5))

'''
v1: (2,4,6)
v2: (3,5,7)
----------------
+: (5,9,13)
-: (-1,-1,-1)
*: (6,20,42)
*: (4,8,12)
'''
