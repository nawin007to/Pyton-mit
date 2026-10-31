students = [
    {"name": "Nawin", "score": 85},
    {"name": "Fox", "score": 92},
    {"name": "Game", "score": 68},
    {"name": "Bank", "score": 75},
]
total = 0
max_score = 0
top_student = ""
for i in students:
    if i["score"] > max_score:
        max_score = i["score"]
        top_student = i["name"]
    total += i["score"]
print(top_student)
print(max_score)
print(total / len(students))