# python3
import itertools

n, m = list(map(int, input().split()))
A = []
for i in range(n):
  A += [list(map(int, input().split()))]
b = list(map(int, input().split()))

clauses = []

for i, coefficient in enumerate(A):
  non_coefficients = [(j, coefficient[j]) for j in range(m) if 0 != coefficient[j]]
  l = len(non_coefficients)

  for x in range(2 ** l):
    current_set = [non_coefficients[j] for j in range(l) if 1 == ((x / 2 ** j) % 2) // 1]
    current_sum = 0
    for coeff in current_set:
      current_sum += coeff[1]
    if current_sum > b[i]:
      clauses.append([-(coeff[0]+1) for coeff in current_set] + [(coeff[0]+1) for coeff in non_coefficients if coeff not in current_set])

if len(clauses) == 0:
  clauses.append([1, -1])
  m = 1

print(len(clauses), m)

for c in clauses:
  c.append(0)
  print(' '.join(map(str, c)))


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
# def printEquisatisfiableSatFormula():
#     print("3 2")
#     print("1 2 0")
#     print("-1 -2 0")
#     print("1 -2 0")

# printEquisatisfiableSatFormula()

