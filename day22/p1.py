import math

f = open("input", "r")
g = map(lambda a: list(a), f.read().splitlines())

x = len(g[0]) / 2
y = len(g) / 2

dx = 0
dy = -1
c = 0
for i in xrange(10000):
  if y < 0:
    g = [['.' for j in xrange(len(g[0]))]] + g
    y += 1
  if y >= len(g):
    g.append(['.' for j in xrange(len(g[0]))])
  if x < 0:
    g = map(lambda r: ['.'] + r, g)
    x += 1
  if x >= len(g[0]):
    g = map(lambda r: r + ['.'], g)

  if g[y][x] == '#':
    t = dx
    dx = -dy
    dy = t
  else:
    t = dx
    dx = dy
    dy = -t

  if g[y][x] == '#':
    g[y][x] = '.'
  else:
    c += 1
    g[y][x] = '#'

  x += dx
  y += dy

print c