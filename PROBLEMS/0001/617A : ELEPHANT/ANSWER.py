data = int(input())

def solve(x: int) -> int:
  if x <= 5:
    return 1
  else:
    d = x//5
    rem x % 5
    if rem > 0:
      return d +1
    else:
      return d

ans = solve(data)
print(data)
