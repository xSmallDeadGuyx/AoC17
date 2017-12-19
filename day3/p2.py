import math

inp = 289326

g = dict()
g[(0, 0)] = 1
x = 0
y = 0
dx = 1
dy = 0

while True:
  x += dx
  y += dy
  n = 0
  for i in xrange(3):
    for j in xrange(3):
      p = (x + i - 1, y + j - 1)
      if p in g:
        n += g[p] 
  if n >= inp:
    print n
    break
  g[(x, y)] = n
  if (x + dy, y - dx) not in g:
    if dx == 1:
      dy = -1
      dx = 0
    elif dx == -1:
      dy = 1
      dx = 0
    elif dy == 1:
      dy = 0
      dx = 1
    else:
      dy = 0
      dx = -1