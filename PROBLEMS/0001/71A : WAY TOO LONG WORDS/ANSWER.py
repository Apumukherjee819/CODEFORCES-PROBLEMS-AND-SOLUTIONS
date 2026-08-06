import sys
data = sys.stdin.read().split()

if len(data) == int(data[0])+1:
	for i in range(1,len(data)):
		if len(data[i]) > 10:
			print(f"{data[i][0]}{len(data[i][1:len(data[i])-1])}{data[i][len(data[i])-1]}")
		else:
			print(data[i])
