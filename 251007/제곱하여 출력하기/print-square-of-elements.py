N = int(input())
M = list(map(int, input().split()))
O = []

for i in M:
    O.append(i**2)
print(' '.join(map(str, O)))

