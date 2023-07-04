from vector3 import Vector3
from vector2 import Vector2
from mathf import Math
from randomf import Random

if __name__ == '__main__':
    a = Vector3(3, 6, 5)
    b = Vector3(4, 1, 5)
    # aa = Vector2(2, 4)
    # bb = Vector2(4, 9)

    # print(f'+: {aa + bb}\n-: {aa - bb}\n*: {aa * bb}')

#     print(f'v1: {v1}\nv2: {v2}\n\
# ----------------\n\
# +: {(v1 + v2)}\n-: {(v1 - v2)}\n\
# *: {(v1 * v2)}\n*: {(v1 * 2)}')

    print(Vector3.distance(a, b))
    # print('cross: ', Vector3.cross(v1, v2))
    # print('dot: ', Vector3.dot(v1, v2))

    # print(Vector3.min(a, b))
    # print(Vector3.max(a, b))

    # print(Math.round(Vector3.distance(v1, v2), 1))

    # _complex = 2 + 2j
    # print(numpy.rad2deg(cmath.phase(_complex)))

    # print("vector3 true kakezan", v1 * v2)
    # # (-2, 4, -2)

    # while True:
    #     r = random.randint(-1, 2)
    #     print(r, Math.clamp(r, 0, 1))

    # for n in range(0, 20, 1):
    #     print(f'{n} is prime: {Math.is_prime2(n)}')
    # print(Random().normal_char(1000))
    #     print('int: ', Random().randint(1, 10))
    #     print('float: ', Random().uniform(1.0, 10))

'''
v1: (2,4,6)
v2: (3,5,7)
----------------
+: (5,9,13)
-: (-1,-1,-1)
*: (6,20,42)
*: (4,8,12)
'''
