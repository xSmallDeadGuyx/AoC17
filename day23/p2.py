import math

f = open("optimised", "r")
p = map(lambda a: a.split(' '), f.read().splitlines())
r = dict()
r['a'] = 1
for i in 'bcdefgh':
  r[i] = 0

def val(x):
  try:
    return int(x)
  except:
    return r[x]

def isPrime(num):
  if num < 2:
    return False
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

i = 0
while i < len(p):
  c = p[i]
  print ' '.join(c)
  if c[0] == 'jp':
    if isPrime(val(c[1])):
      i += val(c[2])
      continue
  if c[0] == 'set':
    r[c[1]] = val(c[2])
  elif c[0] == 'sub':
    r[c[1]] -= val(c[2])
  elif c[0] == 'mul':
    r[c[1]] *= val(c[2])
  elif c[0] == 'jnz':
    if val(c[1]) != 0:
      i += val(c[2])
      continue

  i += 1

print r['h']