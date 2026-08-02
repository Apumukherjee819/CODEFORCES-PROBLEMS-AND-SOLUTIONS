import sys

def main():
    data = sys.stdin.read().split('\n')
    n = int(data[0])
    db = {}  # name -> next suffix to try
    out = []

    for i in range(1, n + 1):
        name = data[i].strip()
        if name not in db:
            out.append("OK")
            db[name] = 1
        else:
            k = db[name]
            while (name + str(k)) in db:
                k += 1
            new_name = name + str(k)
            out.append(new_name)
            db[new_name] = 1      # this generated name could itself be requested later
            db[name] = k + 1      # next time, start searching from here

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    main()
