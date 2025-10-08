A, B = (map(int, input().split()))
num = 0

for i in range (A, B+1):
    if i % 2 == 0:
        num+= i
    else: 
        continue
print(num)
