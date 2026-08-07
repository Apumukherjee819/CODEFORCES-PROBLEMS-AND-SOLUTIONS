import sys
import math
data = sys.stdin.read().split()

total = int(data[0]) * int(data[1])

area = 2
print(math.floor(total//area))
