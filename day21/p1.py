f = open("input", "r")
rules = dict()
rules[2] = dict()
rules[3] = dict()
for l in f.readlines():
  l = l.split(' ')
  if len(l) == 1:
    continue
  target = 2 if len(l[0]) == 5 else 3
  count = l[0].count('#')
  if count not in rules[target]:
    rules[target][count] = []
  rules[target][count].append((l[0], l[2][:-1].split('/')))

def rotate90(x):
  x = x.split('/')
  size = len(x)
  nx = [['.' for j in xrange(size)] for i in xrange(size)]
  for i in xrange(0, size):
    for j in xrange(0, size):
      nx[j][i] = x[size-i-1][j]
  return '/'.join(map(lambda a: ''.join(a), nx))

def getRotations(x):
  x1 = rotate90(x)
  x2 = rotate90(x1)
  x3 = rotate90(x2)
  yield x
  yield x1
  yield x2
  yield x3

current = '.#./..#/###'
for i in xrange(5):
  grid = [[j for j in row] for row in current.split('/')]
  size = 2 if len(grid[0]) % 2 == 0 else 3
  shapes = len(grid[0]) / size
  newSize = shapes * (size + 1)
  newGrid = [['.' for j in xrange(newSize)] for i in xrange(newSize)]
  for i in xrange(shapes):
    for j in xrange(shapes):
      shape = '/'.join(''.join(row[i*size:(i+1)*size]) for row in grid[j*size:(j+1)*size])
      count = shape.count('#')
      flipped = '/'.join(reversed(shape.split('/')))
      tests = list(getRotations(shape)) + list(getRotations(flipped))
      for pattern, result in rules[size][count]:
        found = False
        for test in tests:
          if test == pattern:
            found = True
            for k in xrange(size+1):
              for l in xrange(size+1):
                x = i * (size+1) + k
                y = j * (size+1) + l
                newGrid[y][x] = result[l][k]
            break
        if found:
          break
  current = '/'.join(map(lambda a: ''.join(a), newGrid))

print current.count('#')