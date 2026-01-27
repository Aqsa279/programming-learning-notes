# List & Dictionary Practice (SOC-style examples)

# Program 1: User list
users = [
    {"username": "iqra", "role": "student", "active": True},
    {"username": "ali", "role": "admin", "active": False},
    {"username": "sara", "role": "student", "active": True}
]

print("Active users:")
for user in users:
    if user["active"]:
        print(user["username"])


# Program 2: Login logs analysis
logs = [
    {"ip": "10.0.0.1", "status": "failed"},
    {"ip": "10.0.0.2", "status": "success"},
    {"ip": "10.0.0.3", "status": "failed"}
]

print("\nFailed login alerts:")
for log in logs:
    if log["status"] == "failed":
        print("⚠️ Alert from IP:", log["ip"])


# Program 3: Dictionary update
student = {
    "name": "Iqra",
    "age": 20,
    "course": "BSCS"
}

student["age"] = 21
student["city"] = "Lahore"

print("\nUpdated student info:")
for key in student:
    print(key, "=>", student[key])

