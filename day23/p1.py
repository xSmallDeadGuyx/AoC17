f = open("input", "r")
p = map(lambda a: a.split(' '), f.read().splitlines())
r = dict()
for i in 'abcdefgh':
  r[i] = 0

def val(x):
  try:
    return int(x)
  except:
    return r[x]

i = 0
m = 0
while i < len(p):
  c = p[i]
  if c[0] == 'set':
    r[c[1]] = val(c[2])
  elif c[0] == 'sub':
    r[c[1]] -= val(c[2])
  elif c[0] == 'mul':
    r[c[1]] *= val(c[2])
    m += 1
  elif c[0] == 'jnz':
    if val(c[1]) != 0:
      i += val(c[2])
      continue

  i += 1

print m