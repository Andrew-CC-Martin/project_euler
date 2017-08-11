def no_factors(num):
  
  total = 0
  i = 1
  sqrt = int((num ** 0.5))

  while i <= sqrt:
    if num % i == 0:
      total += 1
    i += 1
  return total * 2

'''for i in range(20):
  
  print(i)
  print(no_factors(i))
  print("")
'''

i = 3
highest = 0
while highest < 200:
  temp = no_factors(i)
  if temp > highest:
    highest = temp
  i += 1
print(i - 1)
