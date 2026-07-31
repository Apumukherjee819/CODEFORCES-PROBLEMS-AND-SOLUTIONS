import sys

def solve():
    data = sys.stdin.read().split()
    vals = list(map(float, data))
    x1, y1, r1 = vals[0], vals[1], vals[2]
    x2, y2, r2 = vals[3], vals[4], vals[5]
    x3, y3, r3 = vals[6], vals[7], vals[8]

    EPS = 1e-9

    def locus(xi, yi, ri, xj, yj, rj):
        # Locus of points P with |P-Ci|/ri = |P-Cj|/rj.
        # Returns A, D, E, F for  A*(x^2+y^2) + D*x + E*y + F = 0
        # (A circle if A != 0, a line if A == 0.)
        A = rj * rj - ri * ri
        D = -2 * (rj * rj * xi - ri * ri * xj)
        E = -2 * (rj * rj * yi - ri * ri * yj)
        F = rj * rj * (xi * xi + yi * yi) - ri * ri * (xj * xj + yj * yj)
        return A, D, E, F

    A1, D1, E1, F1 = locus(x1, y1, r1, x2, y2, r2)
    A2, D2, E2, F2 = locus(x1, y1, r1, x3, y3, r3)

    def solve_line_line(a1, b1, c1, a2, b2, c2):
        det = a1 * b2 - a2 * b1
        if abs(det) < 1e-12:
            return []
        x = (-c1 * b2 + c2 * b1) / det
        y = (-a1 * c2 + a2 * c1) / det
        return [(x, y)]

    def solve_line_circle(a, b, c, A, D, E, F):
        cx = -D / (2 * A)
        cy = -E / (2 * A)
        r2_ = cx * cx + cy * cy - F / A
        if r2_ < -1e-7:
            return []
        r2_ = max(r2_, 0.0)
        rad = r2_ ** 0.5
        if abs(a) < 1e-15 and abs(b) < 1e-15:
            return []
        norm2 = a * a + b * b
        t = -(a * cx + b * cy + c) / norm2
        fx, fy = cx + a * t, cy + b * t
        dist2 = (fx - cx) ** 2 + (fy - cy) ** 2
        rem = rad * rad - dist2
        if rem < -1e-7:
            return []
        rem = max(rem, 0.0)
        dirx, diry = -b, a
        dn = (dirx * dirx + diry * diry) ** 0.5
        dirx, diry = dirx / dn, diry / dn
        s = rem ** 0.5
        p1 = (fx + dirx * s, fy + diry * s)
        p2 = (fx - dirx * s, fy - diry * s)
        if s < 1e-9:
            return [p1]
        return [p1, p2]

    if abs(A1) < EPS and abs(A2) < EPS:
        points = solve_line_line(D1, E1, F1, D2, E2, F2)
    else:
        a = A2 * D1 - A1 * D2
        b = A2 * E1 - A1 * E2
        c = A2 * F1 - A1 * F2
        if abs(A1) > EPS:
            points = solve_line_circle(a, b, c, A1, D1, E1, F1)
        else:
            points = solve_line_circle(a, b, c, A2, D2, E2, F2)

    best = None
    for (px, py) in points:
        d1 = ((px - x1) ** 2 + (py - y1) ** 2) ** 0.5
        k1 = d1 / r1
        if k1 < 1 - 1e-6:
            continue  # point would be inside stadium 1 (and thus 2, 3) - invalid
        if best is None or k1 < best[0]:
            best = (k1, px, py)

    if best is not None:
        def fmt(v):
            v = round(v, 5)
            if v == 0:
                v = 0.0
            return f"{v:.5f}"
        print(f"{fmt(best[1])} {fmt(best[2])}")

solve()
