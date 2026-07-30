import sys
import math

def solve():
    data = sys.stdin.read().split()
    x1, y1, x2, y2, x3, y3 = map(float, data[:6])
    p1, p2, p3 = (x1, y1), (x2, y2), (x3, y3)

    def dist(p, q):
        return math.hypot(p[0]-q[0], p[1]-q[1])

    # side lengths (a opposite p1, b opposite p2, c opposite p3)
    a = dist(p2, p3)
    b = dist(p1, p3)
    c = dist(p1, p2)

    # interior angles of the triangle at each vertex, via law of cosines
    A = math.acos((b*b + c*c - a*a) / (2*b*c))
    B = math.acos((a*a + c*c - b*b) / (2*a*c))
    C = math.pi - A - B

    # circumradius of the triangle (= circumradius of the regular polygon)
    R = a / (2 * math.sin(A))

    def fgcd(x, y, eps=1e-4):
        while y > eps:
            x, y = y, math.fmod(x, y)
        return x

    # each triangle angle is k * (pi/n) for the same base unit theta = pi/n
    theta = fgcd(fgcd(A, B), C)
    n = round(math.pi / theta)

    area = 0.5 * n * R * R * math.sin(2 * math.pi / n)
    print(f"{area:.6f}")

solve()
