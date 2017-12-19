f = open("input", "r")
p = dict()
for l in f.readlines():
  l = l.split()
  r = l[0]
  if r not in p:
    p[r] = 0
  d = 1 if l[1] == 'inc' else -1
  n = int(l[2])
  c = l[4]
  if c not in p:
    p[c] = 0
  x = int(l[6])
  e = False
  if l[5] == '==':
    e = p[c] == x
  if l[5] == '!=':
    e = p[c] != x
  if l[5] == '>=':
    e = p[c] >= x
  if l[5] == '<=':
    e = p[c] <= x
  if l[5] == '>':
    e = p[c] > x
  if l[5] == '<':
    e = p[c] < x

  if e:
    p[r] += n * d

m = None
for r, v in p.iteritems():
  if m is None or v > m:
    m = v

print m