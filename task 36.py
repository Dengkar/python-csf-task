score = input(int())
user_score = int(score)
if user_score >= 90:
    print("A")
if 80 < user_score < 89:
    print("B")
if 70 < user_score < 79:
    print("C")
if 60 < user_score < 69:
    print("D")
if user_score < 60:
    print("F")
else:
    print("invalid score")
