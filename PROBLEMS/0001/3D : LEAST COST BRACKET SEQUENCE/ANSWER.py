import heapq

def solve():
    pattern = input().strip()
    n = len(pattern)
    m = pattern.count('?')

    a = [0] * m
    b = [0] * m
    for i in range(m):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi

    chars = list(pattern)
    total = 0
    balance = 0
    heap = []  # stores (a_i - b_i, position_in_chars)
    q = 0      # index into a[]/b[] arrays

    for i in range(n):
        c = chars[i]
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
        else:  # '?'
            ai, bi = a[q], b[q]
            q += 1
            chars[i] = ')'          # tentatively close it
            total += bi
            balance -= 1
            heapq.heappush(heap, (ai - bi, i))

        if balance < 0:
            if not heap:
                print(-1)
                return
            diff, pos = heapq.heappop(heap)
            total += diff
            chars[pos] = '('
            balance += 2            # flipping ')' -> '(' changes balance by +2

    if balance != 0:
        print(-1)
        return

    print(total)
    print(''.join(chars))

solve()
