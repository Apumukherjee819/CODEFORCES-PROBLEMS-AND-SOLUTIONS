import sys
data = sys.stdin.read().split()
x = int(data[0])
y = int(data[1])

def solve(a:int,b:int)-> int:
	if a > b:
		return 0
	elif a == b:
		return 1
	else:
		count = 0
		while a <= b:
			a *= 3
			b *= 2
			count += 1
		return count
	
	
ans = solve(x,y)
print(ans)
 
