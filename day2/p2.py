import math

f = open("input", "r")
x = 0
for l in f.readlines():
  a = sorted(map(int, l.split()))[::-1]
  if len(a):
    f = False
    for i in xrange(len(a)-1):
      m = math.sqrt(a[i])
      for j in xrange(len(a)-1, 0, -1):
        if a[j] == a[i]:
          break
        if a[i] % a[j] == 0:
          print a[i], a[j], a[i]/a[j]
          x += a[i] / a[j]
          f = True
          break
      if f:
        break
      
print x
