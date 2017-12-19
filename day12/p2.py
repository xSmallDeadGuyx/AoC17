f = open("input", "r")
n = []
for l in f.readlines():
  p = l.split()
  n.append(map(int, ''.join(p[2:]).split(',')))

g = 0
v = set()
while len(v) < len(n):
  p = []
  for i in xrange(len(n)):
    if i not in v:
      p.append(i)
      break
  while len(p) > 0:
    c = p[0]
    v.add(c)
    for i in n[c]:
      if i not in v and i not in p:
        p.append(i)
    p = p[1:]
  g += 1

print g
