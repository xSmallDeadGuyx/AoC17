import math

inp = 289326

lower = int(math.floor(math.sqrt(inp)))
if lower % 2 == 0:
  lower -= 1
ring = (lower - 1) / 2
length = lower + 1
mids = [lower * lower + int(math.floor(length / 2)) + length * i for i in xrange(4)]
print min(map(lambda a: abs(a - inp), mids)) + (ring + 1)