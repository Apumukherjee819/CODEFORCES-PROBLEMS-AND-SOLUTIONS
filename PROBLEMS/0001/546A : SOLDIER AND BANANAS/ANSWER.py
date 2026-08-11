import sys
data = sys.stdin.read().split()

a = int(data[0])
b = int(data[1])
c  = int(data[2])

total = (c*(c+1)//2)*a
print(0 if total <= b else total - b)
