f = open("input", "r")
p = set()
s = set()
for l in f.readlines():
  l = l.split()
  p.add(l[0])
  s = s.union(set(''.join(l[3:]).split(',')))

print p.difference(s)