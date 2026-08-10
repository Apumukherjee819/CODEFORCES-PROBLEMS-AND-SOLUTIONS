import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ns = data[1:1 + t]

    # Sieve of Eratosthenes up to the maximum possible n+1 (2*10^5 + 1)
    MAXN = 200002
    sieve = bytearray([1]) * (MAXN + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(MAXN ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:MAXN+1:i] = bytearray(len(range(i*i, MAXN+1, i)))

    out = []
    for i in range(t):
        n = int(ns[i])
        # A universal winner exists iff (n+1) is prime.
        out.append("YES" if sieve[n + 1] else "NO")

    sys.stdout.write("\n".join(out) + "\n")

solve()
