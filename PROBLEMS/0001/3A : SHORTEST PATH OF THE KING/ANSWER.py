import sys

def solve():
    data = sys.stdin.read().split()
    s, t = data[0], data[1]

    sx, sy = ord(s[0]) - ord('a'), int(s[1]) - 1
    tx, ty = ord(t[0]) - ord('a'), int(t[1]) - 1

    dx, dy = tx - sx, ty - sy
    n = max(abs(dx), abs(dy))

    moves = []
    for _ in range(n):
        step = ''
        if dx > 0:
            step += 'R'
            dx -= 1
        elif dx < 0:
            step += 'L'
            dx += 1
        if dy > 0:
            step += 'U'
            dy -= 1
        elif dy < 0:
            step += 'D'
            dy += 1
        moves.append(step)

    print(n)
    print('\n'.join(moves))

solve()
