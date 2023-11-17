import dataclasses
import numpy as np
from mathf import Math


@dataclasses.dataclass
class Vector3:
    x: float
    y: float
    z: float

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        elif isinstance(other, (float, int)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        raise TypeError()

    def __radd__(self, other):
        if isinstance(other, Vector3):
            return Vector3(other.x + self.x, other.y + self.y, other.z + self.z)
        raise TypeError()

    def __rsub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(other.x - self.x, other.y - self.y, other.z - self.z)
        raise TypeError()

    def __str__(self) -> str:
        return f'({self.x},{self.y},{self.z})'

    def cross(a, b): return a * b

    def dot(a, b): return a.x * b.x + a.y * b.y + a.z * b.z

    def normalize(self):
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def distance(a, b):
        return Vector3.normalize(a-b)

    def min(a, b):
        return Vector3(Math.min(a.x, b.x), Math.min(a.y, b.y), Math.min(a.z, b.z))

    def max(a, b):
        return Vector3(Math.max(a.x, b.x), Math.max(a.y, b.y), Math.max(a.z, b.z))


ZERO = Vector3(0, 0)
ONE = Vector3(1, 1)
X = Vector3(1, 0)
Y = Vector3(0, 1)

""" 
https://yumarublog.com/python/operator/
http://www.math.s.chiba-u.ac.jp/~yasuda/Chiba/Lec/naiseki.pdf
"""
