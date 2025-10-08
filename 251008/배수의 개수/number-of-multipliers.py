A = []
for num in range(10):
    A.append(int(input()))

three=[]
five= []

for i in A:
    if i % 3 == 0:
        three.append(i)
for i in A:
    if i % 5 == 0:
        five.append(i)
print(len(three), end=" ")
print(len(five))