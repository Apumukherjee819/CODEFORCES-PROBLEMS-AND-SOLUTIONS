import sys

data = sys.stdin.read().split('\n')
input_data = [ele.split() for ele in data[:len(data)-1:]]
def solve(nums)-> list:
  for i in range(5):
    for j in range(5):
      if nums[i][j] == '1':
        return [i,j]

print(abs(2-position(input_data)[0])+abs(2-position(input_data)[1]))
