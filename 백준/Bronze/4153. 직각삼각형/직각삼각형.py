while True:
  a, b, c = map(int, input().split())
  if a == b == c == 0:
      break
  max_side = max(a, b, c)
  if max_side**2 == (a**2 + b**2 + c**2 - max_side**2):
      print('right')
  else:
      print('wrong')
