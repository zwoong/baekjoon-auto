T = int(input())

for _ in range(T):
    stack = []
    parenthesis_string = input()

    for char in parenthesis_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else: 
        if not stack:
            print("YES")
        else:
            print("NO")
