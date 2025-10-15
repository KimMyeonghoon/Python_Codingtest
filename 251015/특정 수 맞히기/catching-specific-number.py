count = 0 
while count<3 :
    num=int(input())
    count+=1
    if num < 25 :
        print("Higher")
    elif num > 25:
        print("Lower")
    else:
        print("Good")

    