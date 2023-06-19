from mathf import Math
import numpy as np


class Vector2:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return self.x * other.y - self.y * other.x
        elif isinstance(other, (float, int)):
            return self.x * other.x + self.y * other.y
        raise TypeError()

    def __radd__(self, other):
        if isinstance(other, Vector2):
            return Vector2(other.x + self.x, other.y + self.y)
        raise TypeError()

    def __rsub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(other.x - self.x, other.y - self.y)
        raise TypeError()

    def __str__(self) -> str:
        # return f'({self.x},{self.y})'
        return f'(x:{self.x}, y:{self.y})'

    def set(self, x, y, z):
        self.x = x
        self.y = y

    def cross(a, b): return a * b

    def dot(a, b): return a.x * b.x + a.y * b.y

    def distance(a, b) -> float:
        if isinstance(a, Vector2) and isinstance(b, Vector2):
            return np.round(np.sqrt(np.power(a.x - b.x, 2) + np.power(a.y - b.y, 2)), 3)
        raise TypeError()

    def min(a, b):
        if isinstance(a, Vector2) and isinstance(b, Vector2):
            return Vector2(Math.min(a.x, b.x), Math.min(a.y, b.y))
        raise TypeError()

    def max(a, b):
        if isinstance(a, Vector2) and isinstance(b, Vector2):
            return Vector2(Math.max(a.x, b.x), Math.max(a.y, b.y))
        raise TypeError()

    def zero(): return Vector2(0, 0)

    def one(): return Vector2(1, 1)

    def up(): return Vector2(0, 1)

    def right(): return Vector2(1, 0)
