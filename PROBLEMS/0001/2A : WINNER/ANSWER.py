from collections import defaultdict

n = int(input())

rounds = []
final_score = defaultdict(int)

# Read input and calculate final scores
for _ in range(n):
    name, score = input().split()
    score = int(score)
    rounds.append((name, score))
    final_score[name] += score

# Maximum final score
mx = max(final_score.values())

# Find the winner
current_score = defaultdict(int)

for name, score in rounds:
    current_score[name] += score
    if current_score[name] >= mx and final_score[name] == mx:
        print(name)
        break
