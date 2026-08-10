data = input()
data = data.split('+')
inp = [int(ele) for ele in data]
inp.sort()
d = [str(ele) for ele in inp]
print("+".join(d))
