p = [0 for _ in range(101)]
p[1], p[2], p[3] = 1, 1, 1
for i in range(4, 101):
  p[i] = p[i-3] + p[i-2]

t = int(input())
for _ in range(t):
  n = int(input())
  print(p[n])