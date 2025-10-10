N = int(input())

for i in range(1,N+1):
        for j in range(1, 4):
             print(f"{i} x {j} = {i*j}", end=", ")
        print("",sep="\n" )