f = open("input", "r")
x = 0
for l in f.readlines():
  a = sorted(map(int, l.split()))
  if len(a):
    x += a[-1] - a[0]
print x
