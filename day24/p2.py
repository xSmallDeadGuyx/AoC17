f = open("input", "r")
pieces = map(lambda a: map(int, a.split('/')), f.read().splitlines())

ls = 0
ll = []
def go(l, s, c, p):
  global ls, ll
  for i in xrange(len(p)):
    ps = p[i][0] + p[i][1]
    r = 0
    np = p[:]
    del np[i]
    if p[i][0] == c:
      r = s + ps
      go(l + 1, s + ps, p[i][1], np)
    elif p[i][1] == c:
      r = s + ps
      go(l + 1, s + ps, p[i][0], np)
    if r != 0:
      if l + 1 > ls:
        ls = l + 1
        ll = [r]
      elif l + 1 == ls:
        ll.append(r)

go(0, 0, 0, pieces)
print reduce(max, ll)