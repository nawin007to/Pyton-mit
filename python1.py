
login_logs = [
    {"user": "nawin", "success": False},
    {"user": "fox", "success": True},
    {"user": "nawin", "success": False},
    {"user": "fox", "success": False},
    {"user": "nawin", "success": False},
    {"user": "fox", "success": False},
]

failed_count = {}

# ขั้นที่ 1: นับจำนวนครั้งที่ล็อกอินไม่สำเร็จ
for i in login_logs:
    name = i["user"]
    success = i["success"]

    if success == False:
        if name in failed_count:
            failed_count[name] += 1
        else:
            failed_count[name] = 1

# ขั้นที่ 2: แสดงเฉพาะคนที่ผิดตั้งแต่ 3 ครั้งขึ้นไป
for name, count in failed_count.items():
    if count >= 3:
        print(f"{name}: {count} failed attempts")
