f = open("input", "r")
s = f.read().splitlines()

c = s[0][15]
n = int(s[1].split(' ')[5])

del s[:2]

r = dict()

for i in xrange(len(s)/10):
  j = i * 10 + 1
  x = s[j][9]
  zeroCmds = dict()
  zeroCmds['w'] = 1 if '1' in s[j+2] else 0
  zeroCmds['m'] = 1 if 'right' in s[j+3] else -1
  zeroCmds['s'] = s[j+4].split(' ')[8][0]

  oneCmds = dict()
  oneCmds['w'] = 1 if '1' in s[j+6] else 0
  oneCmds['m'] = 1 if 'right' in s[j+7] else -1
  oneCmds['s'] = s[j+8].split(' ')[8][0]
  r[x] = [zeroCmds, oneCmds]

p = 0
t = [0]
for i in xrange(n):
  if p < 0:
    t = [0] + t
    p += 1
  if p == len(t):
    t.append(0)

  i = r[c][t[p]]
  t[p] = i['w']
  p += i['m']
  c = i['s']
print t.count(1)