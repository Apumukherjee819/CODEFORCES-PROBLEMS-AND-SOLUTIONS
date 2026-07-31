import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    v = int(data[idx]); idx += 1

    kayaks = []      # (capacity, original_index)
    catamarans = []  # (capacity, original_index)

    for i in range(1, n + 1):
        t = int(data[idx]); idx += 1
        p = int(data[idx]); idx += 1
        if t == 1:
            kayaks.append((p, i))
        else:
            catamarans.append((p, i))

    # sort descending by capacity (best first)
    kayaks.sort(key=lambda x: -x[0])
    catamarans.sort(key=lambda x: -x[0])

    num_kayak = len(kayaks)
    num_cat = len(catamarans)

    prefix_kayak = [0] * (num_kayak + 1)
    for i in range(num_kayak):
        prefix_kayak[i + 1] = prefix_kayak[i] + kayaks[i][0]

    prefix_cat = [0] * (num_cat + 1)
    for i in range(num_cat):
        prefix_cat[i + 1] = prefix_cat[i] + catamarans[i][0]

    max_k = min(num_cat, v // 2)

    best_total = -1
    best_k = 0
    best_m = 0

    for k in range(0, max_k + 1):
        remaining = v - 2 * k
        m = min(remaining, num_kayak)
        total = prefix_cat[k] + prefix_kayak[m]
        if total > best_total:
            best_total = total
            best_k = k
            best_m = m

    if best_total == -1:
        best_total = 0

    chosen = [catamarans[i][1] for i in range(best_k)] + [kayaks[i][1] for i in range(best_m)]

    out = []
    out.append(str(best_total))
    out.append(' '.join(map(str, chosen)))
    print('\n'.join(out))

main()
