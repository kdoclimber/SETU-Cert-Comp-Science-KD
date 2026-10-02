score_total = 0
score_count = 0

def add_score():
    global score_total, score_count
    raw = input("Enter score: ")
    score = float(raw)
    score_total += score
    score_count += 1
    print(f"Running average: {score_total / score_count:.1f}")

for _ in range(3):
    add_score()