f = open("input", "r")
pieces = map(lambda a: map(int, a.split('/')), f.read().splitlines())

def go(s, c, p):
  m = s
  for i in xrange(len(p)):
    ps = p[i][0] + p[i][1]
    r = 0
    np = p[:]
    del np[i]
    if p[i][0] == c:
      r = go(s + ps, p[i][1], np)
    elif p[i][1] == c:
      r = go(s + ps, p[i][0], np)
    if r > m:
      m = r
  return m

print go(0, 0, pieces)