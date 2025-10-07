score = (int(input()))
num=[]

for i in range (score, 101, 1):
    if 90<= i < 101:
        print("A", end=" ")
    elif 80<= i < 90:
        print("B", end=" ") 
    elif 70<= i < 80:
        print("C", end=" ") 
    elif 60<= i < 70:
        print("D", end=" ") 
    else :
        print("F", end=" ")
    num.append(i)

