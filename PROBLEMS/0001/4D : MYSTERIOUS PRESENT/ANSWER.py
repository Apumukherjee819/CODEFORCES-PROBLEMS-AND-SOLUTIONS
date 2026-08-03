import sys
from bisect import bisect_left

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    w = int(data[idx]); idx += 1
    h = int(data[idx]); idx += 1

    envelopes = []
    for i in range(n):
        wi = int(data[idx]); idx += 1
        hi = int(data[idx]); idx += 1
        envelopes.append((wi, hi, i + 1))  # keep original 1-based index

    # keep only envelopes that can actually contain the card
    filtered = [e for e in envelopes if e[0] > w and e[1] > h]

    if not filtered:
        print(0)
        return

    # sort by width ascending; for equal width, sort by height DESCENDING
    # (this guarantees the LIS-on-heights step below never picks two
    # envelopes that share the same width)
    filtered.sort(key=lambda e: (e[0], -e[1]))

    m = len(filtered)
    tails_val = []   # increasing tail heights of the best chains found so far
    tails_idx = []   # filtered-array index of the envelope holding each tail
    parent = [-1] * m

    for i in range(m):
        hgt = filtered[i][1]
        pos = bisect_left(tails_val, hgt)
        if pos == len(tails_val):
            tails_val.append(hgt)
            tails_idx.append(i)
        elif hgt < tails_val[pos]:
            tails_val[pos] = hgt
            tails_idx[pos] = i
        # if hgt == tails_val[pos] we keep the earlier envelope (nicer, still valid)
        parent[i] = tails_idx[pos - 1] if pos > 0 else -1

    max_len = len(tails_val)
    cur = tails_idx[-1]

    chain = []
    while cur != -1:
        chain.append(filtered[cur][2])
        cur = parent[cur]
    chain.reverse()

    print(max_len)
    print(' '.join(map(str, chain)))

main()
