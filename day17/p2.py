s = 349
b = [0]
p = 0
c = 0
for i in xrange(0, 50000000):
  p = (p + s) % (i + 1) + 1
  if p == 1:
    c = i + 1
print c