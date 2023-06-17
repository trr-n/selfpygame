from functools import singledispatch
import typing
import numpy as np

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
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z
            )
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Vector3):
            '''tabun gaiseki ?'''
            return Vector3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        elif isinstance(other, (float, int)):
            return Vector3(
                self.x * other,
                self.y * other,
                self.z * other
            )
        raise TypeError()

    def __radd__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                other.x + self.x,
                other.y + self.y,
                other.z + self.z
            )
        raise TypeError()

    def __rsub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                other.x - self.x,
                other.y - self.y,
                other.z - self.z
            )
        raise TypeError()

    def __str__(self) -> str:
        # return f'({self.x},{self.y},{self.z})'
        return f'(x:{self.x}, y:{self.y}, z:{self.z})'

    def distance(v1, v2) -> float:
        if isinstance(v1, Vector3) and isinstance(v2, Vector3):
            diffx = v1.x - v2.x
            diffy = v1.y - v2.y
            diffz = v1.z - v2.z
            return np.round(np.sqrt(
                np.power(diffx, 2) + np.power(diffy, 2) + np.power(diffz, 2)), 3)
        raise TypeError()
