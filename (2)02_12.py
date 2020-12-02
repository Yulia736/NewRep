4. def power(a, n):
  if n == 0:
    return 1
  if n < 0:
    return 1 / power(a, -n)
  if n % 2 == 0:
    return power(a, n // 2) * power(a, n // 2)
  else:
    return power(a, n - 1) * a

a = int(input())
n = int(input())
print(power(a, n))
