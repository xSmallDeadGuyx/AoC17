f = open("input", "r")
n = 0
for l in f.readlines():
  p = l.split()
  if len(p) == len(set(p)):
    n += 1
print n