import re

f = open("input", "r")
inp = f.readline().split("\n")[0]

s = 0
def count(m):
  global s
  s += len(m.group(1))
  return ''
inp = re.sub(r'<(.*?)>', count, re.sub(r'!.', '', inp))
print s