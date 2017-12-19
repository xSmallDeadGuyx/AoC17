s = 349
b = [0]
p = 0
for i in xrange(0, 2017):
  p = (p + s) % len(b) + 1
  b.insert(p, i + 1)
print b[p + 1]