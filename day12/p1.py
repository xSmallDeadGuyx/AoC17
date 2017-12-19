f = open("input", "r")
n = []
for l in f.readlines():
  p = l.split()
  n.append(map(int, ''.join(p[2:]).split(',')))

v = set()
p = [0]
while len(p) > 0:
  c = p[0]
  v.add(c)
  for i in n[c]:
    if i not in v and i not in p:
      p.append(i)
  p = p[1:]

print len(v)
