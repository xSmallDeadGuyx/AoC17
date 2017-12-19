inp = "hwlqcszp"
s = 0
for n in xrange(128):
  v = [ord(x) for x in (inp + "-" + str(n))]
  v += [17, 31, 73, 47, 23]
  l = range(256)

  pos = 0
  skip = 0
  for i in xrange(64):
    for length in v:
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

  for a in o:
    if a >= 128:
      s += 1
      a -= 128
    if a >= 64:
      s += 1
      a -= 64
    if a >= 32:
      s += 1
      a -= 32
    if a >= 16:
      s += 1
      a -= 16
    if a >= 8:
      s += 1
      a -= 8
    if a >= 4:
      s += 1
      a -= 4
    if a >= 2:
      s += 1
      a -= 2
    if a == 1:
      s += 1

print s