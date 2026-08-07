import sys

data = sys.stdin.read().split()

def solve(k : int,nums:list) -> int:
	count = 0
	for ele in nums:
		if int(ele) >= int(nums[k-1]) and int(ele) > 0:
			count += 1
			
	return count
ans =  solve(int(data[1]),data[2::])
print(ans)

