f = open("input", "r")
p = []
for l in f.readlines():
  p.append(l.split())

r = dict()

def val(x):
  global r
  try:
    n = int(x)
    return n
  except ValueError:
    if x not in r:
      r[x] = 0
    return r[x]

i = 0
l = 0
while i < len(p):
  c = p[i]
  if c[0] == 'snd':
    l = val(c[1])
  elif c[0] == 'set':
    r[c[1]] = val(c[2])
  elif c[0] == 'add':
    r[c[1]] = val(c[1]) + val(c[2])
  elif c[0] == 'mul':
    r[c[1]] = val(c[1]) * val(c[2])
  elif c[0] == 'mod':
    r[c[1]] = val(c[1]) % val(c[2])
  elif c[0] == 'rcv':
    print l
    break
  elif c[0] == 'jgz':
    if val(c[1]) > 0:
      i += val(c[2])
      continue
  i += 1
