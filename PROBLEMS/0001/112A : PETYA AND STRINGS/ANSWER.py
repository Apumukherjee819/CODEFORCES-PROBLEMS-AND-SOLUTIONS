import sys
data = sys.stdin.read().split()
if data[0].lower() == data[1].lower():
	print(0)
elif data[0].lower() > data[1].lower():
	print(1)
else:
	print(-1)
