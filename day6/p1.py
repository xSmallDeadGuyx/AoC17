inp = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
s = set()
s.add(tuple(inp))
c = 0
while True:
  m = 0
  j = 0
  for i in xrange(len(inp)):
    if inp[i] > m:
      m = inp[i]
      j = i
  inp[j] = 0
  while m > 0:
    j = (j + 1) % len(inp)
    inp[j] += 1
    m -= 1

  c += 1
  t = tuple(inp)
  if t in s:
    print c
    break
  s.add(t)