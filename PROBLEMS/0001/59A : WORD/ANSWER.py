data = input()
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ucnt = 0
lcnt = 0
for ele in data:
	if ele in upper:
		ucnt += 1
	else:
		lcnt += 1
		
if lcnt >= ucnt :
	print(data.lower())
else:
	print(data.upper())
