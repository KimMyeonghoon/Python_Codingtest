N = int(input())
M = map(int, input().split())
H = []


for i in M:
    if i % 2 == 0:
        H.append(i)
    else : 
        pass
H.reverse()
print(" ".join(map(str, H))) 
