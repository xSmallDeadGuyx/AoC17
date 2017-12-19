f = open("input", "r")
s = 0
for l in f.readlines():
  p = map(int, l.split(': '))
  if p[0] % ((p[1] - 1) * 2) == 0:
    s += p[0] * p[1]

print s
