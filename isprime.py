def is_prime(n):
  if n % 2 == 0 or n < 3:
    return False
  i = int(n ** 0.5)
  while i > 2:
    if n % i == 0:
      return False
    i -= 1
  return True
