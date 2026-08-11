import sys
data = sys.stdin.read().split()

a = int(data[0])
b = int(data[1])


def solve(x : int,y : int) -> int:
	while y> 0:
		if x % 10 == 0:
			x //= 10
		else:
			x -= 1
		y -= 1
		
	return x

ans =  solve(a,b)
print(ans)
