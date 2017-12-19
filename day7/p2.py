nodes = dict()

class Node:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
    self.holding = []

  def getWeight(self):
    global nodes
    w = self.weight
    for n in self.holding:
      w += nodes[n].getWeight()
    return w

p = set()
s = set()
f = open("input", "r")
for l in f.readlines():
  l = l.split()
  n = l[0]
  w = int(l[1][1:-1])
  nodes[n] = Node(n, w)
  if len(l) > 2:
    nodes[n].holding = ''.join(l[3:]).split(',')
    s = s.union(set(nodes[n].holding))

  p.add(n)

current = nodes[list(p.difference(s))[0]]
target = None
while True:
  weights = dict()
  for h in current.holding:
    w = nodes[h].getWeight()
    if w in weights:
      weights[w].append(h)
    else:
      weights[w] = [h]
  print weights

  other = None
  found = False
  for w, l in weights.iteritems():
    if len(l) == 1:
      current = nodes[l[0]]
      found = True
    else:
      other = w

  if not found:
    print current.name, 'is the incorrect one'
    print target, current.weight, current.getWeight()
    print 'Needs to be:', target - (current.getWeight() - current.weight)
    break
  else:
    target = other
