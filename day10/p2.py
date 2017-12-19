inp = [ord(x) for x in "147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70"]
inp += [17, 31, 73, 47, 23]
l = range(256)

pos = 0
skip = 0
for i in xrange(64):
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

o = list()
for i in xrange(len(l)/16):
  o.append(reduce(lambda a, b: a^b, l[i*16:(i+1)*16]))

print "".join(map(lambda a: format(a, "02x"), o))