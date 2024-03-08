while True:
  stack = []
  expression = input()
  if expression == ".":
      break
  for char in expression:
      if char in "([": 
          stack.append(char)
      elif char in ")]":
          if not stack:
              print("no")
              break
          elif (char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "["):
              stack.pop() 
          else:
              print("no")
              break
  else:  
      if not stack:
          print("yes")
      else:
          print("no")
