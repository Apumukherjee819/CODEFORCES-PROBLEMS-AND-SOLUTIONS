n = int(input())

def solve(x:int) -> int:
    ans = 0
    while x > 0:
        if x >= 100:
            x -= 100
            ans += 1
        elif x >= 20:
            x -= 20
            ans += 1
        elif x >= 10:
            x -= 10
            ans += 1
        elif x >= 5:
            x -= 5
            ans += 1
        else:
            x -= 1
            ans += 1
    return ans
answer = solve(n)
print(answer)
