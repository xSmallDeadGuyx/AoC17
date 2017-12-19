f = open("input", "r")
j = []
for l in f.readlines():
  j.append(int(l))

c = 0
i = 0
while i < len(j):
  c += 1
  n = j[i]
  j[i] += 1
  i += n
print c