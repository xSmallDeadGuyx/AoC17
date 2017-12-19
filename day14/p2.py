inp = "hwlqcszp"
g = []
for n in xrange(128):
  v = [ord(x) for x in (inp + "-" + str(n))]
  v += [17, 31, 73, 47, 23]
  l = range(256)

  pos = 0
  skip = 0
  for i in xrange(64):
    for length in v:
      end = pos + length
      if end >= len(l):
        newL = list(reversed(l[pos:] + l[:end%len(l)]))
        l[pos:] = newL[:len(l)-pos]
        l[:end%len(l)] = newL[len(l)-pos:]
      else:
        l[pos:end] = list(reversed(l[pos:end]))
      pos = (pos + length + skip) % len(l)
      skip += 1

  o = list()
  for i in xrange(len(l)/16):
    o.append(reduce(lambda a, b: a^b, l[i*16:(i+1)*16]))

  g.append([])
  for a in o:
    g[n].extend('{:08b}'.format(a)[:])

v = [[False for i in xrange(128)] for j in xrange(128)]
c = 0

def flood(x, y):
  global g, v
  v[y][x] = True
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx > 127 or ny < 0 or ny > 127:
      continue
    if g[ny][nx] == '1':
      if not v[ny][nx]:
        flood(nx, ny)

for y in xrange(128):
  for x in xrange(128):
    if g[y][x] == '1' and not v[y][x]:
      c += 1
      flood(x, y)

print c