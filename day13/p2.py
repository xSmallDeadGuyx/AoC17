f = open("input", "r")
w = []
for l in f.readlines():
  w.append(map(int, l.split(': ')))

d = 0
while True:
  d += 1
  c = False
  for l in w:
    if (l[0] + d) % ((l[1] - 1) * 2) == 0:
      c = True
      break
  if not c:
    print d
    break
