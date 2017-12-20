import math

f = open("input", "r")
am = 0
vm = 0
n = -1
i = 0
for l in f.readlines():
  v = map(int, l.split(', ')[1][3:-1].split(','))
  v = math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
  a = map(int, l.split(', ')[2][3:-2].split(','))
  a = math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
  if n == -1 or a < am or (a == am and v < vm):
    n = i
    am = a
    vm = v
  i += 1

print n