import math

fa = 16807
fb = 48271
ca = 516
cb = 190
m = math.pow(2, 16)
c = 0

for i in xrange(5000000):
  ca = (ca * fa) % 2147483647
  while ca % 4 > 0:
    ca = (ca * fa) % 2147483647
  cb = (cb * fb) % 2147483647
  while cb % 8 > 0:
    cb = (cb * fb) % 2147483647

  if (ca % m) == (cb % m):
    c += 1

print c