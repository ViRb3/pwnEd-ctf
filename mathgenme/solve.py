from z3 import *

solver = Solver()

s = [BitVec(f"flag_{i:02}", 8) for i in range(0, 48)]
v6 = [BitVec(f"key_{i:02}", 8) for i in range(0, 48)]
v5 = 0

for i in range(0, 12):
    solver.add(v6[v5] == (33 * s[v5 + 3] + 89 * s[v5 + 2] + 103 * s[v5 + 1] + 66 * s[v5]))
    solver.add(v6[v5 + 1] == (73 * s[v5] + -125 * s[v5 + 1] + -103 * s[v5 + 2] + 51 * s[v5 + 3]))
    solver.add(v6[v5 + 2] == (113 * s[v5 + 1] + s[v5 + 3] + 54 * s[v5] + 8 * s[v5 + 2]))
    solver.add(v6[v5 + 3] == (25 * s[v5 + 2] + 23 * s[v5 + 3] + 119 * s[v5] + 3 * s[v5 + 1]))
    v5 += 4

key = "04b2fc467e104c0c610e3bf0a009a9f3621905df1997ce0b6cd6a3ea68af4d4deaaf024906f7b259ba32035ac4dad586"
key = [int(x) for x in bytearray.fromhex(key)]
for i in range(0, len(key)):
    solver.add(v6[i] == key[i])
    # multiple solutions, limit flag to ascii range
    solver.add(s[i] >= 32)
    solver.add(s[i] <= 126)

if not solver.check():
    print("No solution")
    exit(0)
m = solver.model()

solution = sorted([(d, m[d]) for d in m], key=lambda x: str(x[0]))
filtered_solution = [x for x in solution if str(x[0]).startswith("flag")]
flag = ''.join(map(lambda x: chr(int(str(x[1]), 10)), filtered_solution))

# print(solution)
print(flag)
