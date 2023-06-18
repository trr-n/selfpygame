from functools import singledispatch
import typing
import numpy as np
from mathf import Math

#? オペレーター https://yumarublog.com/python/operator/
#? 三次元ベクトルの内積,外積 http://www.math.s.chiba-u.ac.jp/~yasuda/Chiba/Lec/naiseki.pdf

class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x: float = x
        self.y: float = y
        self.z: float = z

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
        # return f'({self.x},{self.y},{self.z})'
        return f'(x:{self.x}, y:{self.y}, z:{self.z})'

    def set(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cross(a, b): return a * b

    def dot(a, b): return a.x * b.x + a.y * b.y + a.z * b.z

    def distance(a, b) -> float:
        if isinstance(a, Vector3) and isinstance(b, Vector3):
            return np.round(np.sqrt(
                np.power(a.x - b.x, 2) + np.power(a.y - b.y, 2) + np.power(a.z - b.z, 2)), 3)
        raise TypeError()

    def min(a, b): 
        if isinstance(a, Vector3) and isinstance(b, Vector3):
            return Vector3(Math.min(a.x, b.x), Math.min(a.y, b.y), Math.min(a.z, b.z))
        raise TypeError()

    def max(a, b): 
        if isinstance(a, Vector3) and isinstance(b, Vector3):
            return Vector3(Math.max(a.x, b.x), Math.max(a.y, b.y), Math.max(a.z, b.z))
        raise TypeError()

    def zero(): return Vector3(0, 0, 0)

    def one(): return Vector3(1, 1, 1)

    def up(): return Vector3(0, 1, 0)

    def right(): return Vector3(1, 0, 0)
