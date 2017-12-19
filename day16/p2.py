f = open("input", "r")
inp = f.readline().split("\n")[0].split(',')
p = list('abcdefghijklmnop')
v = list()
v.append(''.join(p))
while True:
  for c in inp:
    if c[0] == 's':
      num = int(c[1:])
      p = p[len(p) - num:] + p[:len(p) - num]
    elif c[0] == 'x':
      x = c[1:].split('/')
      n1 = int(x[0])
      n2 = int(x[1])
      t = p[n1]
      p[n1] = p[n2]
      p[n2] = t
    elif c[0] == 'p':
      x = c[1:].split('/')
      n1 = p.index(x[0])
      n2 = p.index(x[1])
      t = p[n1]
      p[n1] = p[n2]
      p[n2] = t

  w = ''.join(p)
  if w in v:
    print v[1000000000 % len(v)]
    break
  v.append(w)