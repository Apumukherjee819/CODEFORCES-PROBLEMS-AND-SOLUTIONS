import sys
from itertools import combinations

def main():
    sticks = list(map(int, sys.stdin.read().split()))[:4]

    can_triangle = False
    can_segment = False

    for a, b, c in combinations(sticks, 3):
        a, b, c = sorted((a, b, c))
        if a + b > c:
            can_triangle = True
        elif a + b == c:
            can_segment = True

    if can_triangle:
        print("TRIANGLE")
    elif can_segment:
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")

main()
