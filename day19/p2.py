f = open("input", "r")
g = []
for l in f.readlines():
  g.append(list(l))

x = 0
y = 0
dx = 0
dy = 1
for i in xrange(len(g[y])):
  if g[y][i] == '|':
    x = i

s = 0
while True:
  s += 1
  x += dx
  y += dy
  if g[y][x] in '|-ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    continue
  elif g[y][x] == '+':
    if dx != 0:
      dx = 0
      if g[y-1][x] != ' ':
        dy = -1
      else:
        dy = 1
    else:
      dy = 0
      if g[y][x-1] != ' ':
        dx = -1
      else:
        dx = 1
  else:
    break

print s