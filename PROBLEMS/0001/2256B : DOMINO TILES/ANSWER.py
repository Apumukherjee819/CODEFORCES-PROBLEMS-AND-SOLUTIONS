import sys

MOD = 998244353

def count_ways(chain):
    """Return number of valid assignments for a chain of characters
    (each '0', '1', or '?') such that adjacent bits differ."""
    dp0 = dp1 = 0
    for i, ch in enumerate(chain):
        if i == 0:
            if ch == '0':
                dp0 = 1
            elif ch == '1':
                dp1 = 1
            else:  # '?'
                dp0 = 1
                dp1 = 1
        else:
            if ch == '0':
                new_dp0 = dp1
                new_dp1 = 0
            elif ch == '1':
                new_dp0 = 0
                new_dp1 = dp0
            else:  # '?'
                new_dp0 = dp1
                new_dp1 = dp0
            dp0, dp1 = new_dp0 % MOD, new_dp1 % MOD
    return (dp0 + dp1) % MOD

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        s = next(it).strip()
        even_chain = [s[i] for i in range(0, n, 2)]
        odd_chain = [s[i] for i in range(1, n, 2)]
        ways_even = count_ways(even_chain)
        ways_odd = count_ways(odd_chain)
        ans = (ways_even * ways_odd) % MOD
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
