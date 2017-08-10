import isprime

def sum_primes(num):
  total = 0
  i = 2
  while i < num:
    if isprime.is_prime(i):
      total += i
    i += 1
  return total

print(sum_primes(2000000))
