# Loop Practice Programs

# Program 1: Print numbers 1 to 5
for i in range(1, 6):
    print(i)


# Program 2: Print even numbers from list
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        print("Even:", num)


# Program 3: Failed login alert (SOC-style)
logs = ["login ok", "failed login", "login ok", "failed password"]

for log in logs:
    if "failed" in log:
        print("⚠️ Alert:", log)


# Program 4: While loop countdown
count = 5

while count > 0:
    print("Count:", count)
    count -= 1

