import re

f = open("input", "r")
inp = f.readline().split("\n")[0]
inp = re.sub(r'<.*?>', '', re.sub(r'!.', '', inp))

s = 0
d = 0
for i in xrange(len(inp)):
  c = inp[i]
  if c == '{':
    d += 1
  if c == '}':
    s += d
    d -= 1
print s