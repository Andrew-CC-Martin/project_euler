def sum_squares():
  i = 1
  total = 0
  while i < 101:
    total += (i ** 2)
    i += 1
  return total

def square_sum():
  i = 1
  sum = 0
  while i < 101:
    sum += i 
    i += 1
  return sum ** 2
  
difference = square_sum() - sum_squares()
print(difference)
