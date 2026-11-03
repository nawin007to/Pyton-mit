usernames = [
    "nawin123",
    "fox",
    "game@123",
    "bank_456",
    "ab",
    "hello world"
]
for name in usernames:
    valid = True
    if len(name) < 4 or len(name) > 12:
        valid = False
    if " " in name:
        valid = False
    for char in name:
        if not (char.isalnum() or char == "_"):
            valid = False
    if valid:
        print(name, ": Valid")
    else:
        print(name, ": Invalid")
