import sys
data = sys.stdin.read().split()
count = 0
cnt = 0
y = 0
for i in range(1,len(data)):
	if data[i] == '1':
		cnt += 1
	else:
		cnt += 0
	y += 1
	
	if y == 3:
		if cnt >= 2:
			count += 1
		cnt = 0
		y = 0
print(count)
