n = int(input())
count = 0
number = 666

while True:
    if '666' in str(number):
        count += 1
    if count == n:
        print(number)
        break
    number += 1
