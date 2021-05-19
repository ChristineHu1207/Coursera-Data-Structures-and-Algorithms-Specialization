# python3
from sys import stdin
  
def allocate_ads(n, m, A, b, c):  
  # Write your code here
  return [0, [0] * m]

n, m = list(map(int, input().split()))
A = []
for i in range(n):
  A += [list(map(int, input().split()))]
b = list(map(int, input().split()))
c = list(map(int, input().split()))

anst, ansx = allocate_ads(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
