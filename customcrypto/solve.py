from z3 import *

solver = Solver()

enc_raw = [28, 24, 1, 9, 9, 19, 93, 93, 94, 2, 26, 13, 6, 92, 61, 11, 15, 39, 91, 91, 20, 28, 54, 8, 17, 89, 23, 61]
enc = [BitVec(f"enc_{i:02}", 8) for i in range(0, len(enc_raw))]
dec = [BitVec(f"dec_{i:02}", 8) for i in range(0, len(enc_raw))]
key = [BitVec(f"key_{i:02}", 8) for i in range(0, 4)]

# multiple solutions, get the one that starts with known flag format
for i, v in enumerate('pwned'):
    solver.add(dec[i] == ord(v))

for i in range(0, len(enc_raw)):
    solver.add(enc[i] == enc_raw[i])
    chunk = i // 4
    offset = i % 4
    solver.add((dec[i] + chunk) ^ key[offset] == enc[i])
    # multiple solutions, limit flag to ascii range
    solver.add(dec[i] >= 32)
    solver.add(dec[i] <= 126)

if not solver.check():
    print("No solution")
    exit(0)
m = solver.model()

solution = sorted([(d, m[d]) for d in m], key=lambda x: str(x[0]))
filtered_solution = [x for x in solution if str(x[0]).startswith("dec")]
flag = ''.join(map(lambda x: chr(int(str(x[1]), 10)), filtered_solution))

# print(solution)
print(flag)
