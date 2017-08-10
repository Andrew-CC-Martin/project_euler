def get_triplet(total):
  c = total - 3
  b = 2
  a = 1
  while c > 0:
    while b > a:
        if (c ** 2) == ((a ** 2) + (b ** 2)):
          print(a, b, c)
        a += 1
        b -=1
    c -= 1
    b = total - c - 1
    a = 1

get_triplet(1000)

