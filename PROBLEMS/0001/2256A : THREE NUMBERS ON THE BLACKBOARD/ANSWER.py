import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        x, y, z = sorted((a, b, c))
        if x + y <= z:
            out_lines.append(str(y))
        else:
            out_lines.append(str(z - x))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
