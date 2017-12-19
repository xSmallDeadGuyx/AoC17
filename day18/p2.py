f = open("input", "r")
p = []
for l in f.readlines():
  p.append(l.split())

count = 0
class P:
  def __init__(self, id):
    self.id = id
    self.registers = dict()
    self.registers['p'] = id
    self.queue = []
    self.i = 0
    self.ended = False
    self.waiting = False

  def val(self, x):
    try:
      n = int(x)
      return n
    except ValueError:
      if x not in self.registers:
        self.registers[x] = 0
      return self.registers[x]

  def next(self, other):
    if self.ended:
      return
    global p
    global q
    c = p[self.i]
    if c[0] == 'snd':
      if self.id == 1:
        global count
        count += 1
      other.queue.append(self.val(c[1]))
    elif c[0] == 'set':
      self.registers[c[1]] = self.val(c[2])
    elif c[0] == 'add':
      self.registers[c[1]] = self.val(c[1]) + self.val(c[2])
    elif c[0] == 'mul':
      self.registers[c[1]] = self.val(c[1]) * self.val(c[2])
    elif c[0] == 'mod':
      self.registers[c[1]] = self.val(c[1]) % self.val(c[2])
    elif c[0] == 'rcv':
      if len(self.queue) == 0:
        self.waiting = True
        if other.ended or other.waiting:
          self.ended = True
        return
      self.waiting = False
      self.registers[c[1]] = self.queue[0]
      self.queue = self.queue[1:]
    elif c[0] == 'jgz':
      if self.val(c[1]) > 0:
        self.i += self.val(c[2])
        return
    self.i += 1
    if self.i >= len(p):
      self.ended = True

p0 = P(0)
p1 = P(1)
while True:
  p0.next(p1)
  p1.next(p0)
  if p0.ended and p1.ended:
    break
print count