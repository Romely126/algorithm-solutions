subject = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)
adjusted_total = 0
for score in scores:
    adjusted_total += (score / max_score) * 100

average = adjusted_total / subject
print(f"{average:.2f}")
