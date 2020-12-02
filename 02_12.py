1.
a=int(input())
b=int(input())
c=int(input())
d=int(input())
def min4(a,b,c,d):
  return min(min(min(a,b),c),d)
print("Манимальное значение =", min4(a,b,c,d))
2.n = int(input("Введите целое число: "))
max_del = 1
for i in range(n - 1, 1, -1):
    if (n % i == 0):
        if (max_del < i):
            max_del = i
print("Максимальный равен:", max_del)

