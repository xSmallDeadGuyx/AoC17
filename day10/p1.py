inp = map(int, "147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70".split(","))
l = range(256)

pos = 0
skip = 0
for length in inp:
  end = pos + length
  if end >= len(l):
    newL = list(reversed(l[pos:] + l[:end%len(l)]))
    l[pos:] = newL[:len(l)-pos]
    l[:end%len(l)] = newL[len(l)-pos:]
  else:
    l[pos:end] = list(reversed(l[pos:end]))
  pos = (pos + length + skip) % len(l)
  skip += 1

print l[0] * l[1]