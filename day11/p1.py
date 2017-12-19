f = open("input", "r")
inp = f.readline().split("\n")[0].split(",")

x = 0
y = 0
z = 0

for d in inp:
  if d == "n":
    y += 1
    z -= 1
  if d == "s":
    y -= 1
    z += 1
  if d == "ne":
    x += 1
    z -= 1
  if d == "sw":
    x -= 1
    z += 1
  if d == "se":
    x += 1
    y -= 1
  if d == "nw":
    x -= 1
    y += 1

print max(abs(x), abs(y), abs(z))