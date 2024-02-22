num_users = int(input())

users = []
for _ in range(num_users):
    age, name = input().split()
    users.append((int(age), name))

sorted_users = sorted(users, key=lambda x: x[0])
for age, name in sorted_users:
    print(age, name)
