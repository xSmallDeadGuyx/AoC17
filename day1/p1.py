f = open("input", "r")
inp = f.readline().split("\n")[0]
s = 0
for i in xrange(len(inp)):
  j = (i + 1) % len(inp)
  if inp[i] == inp[j]:
    s += int(inp[i])
print s
