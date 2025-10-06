Y = int(input())

if Y % 100 == 0 :
     if Y % 400 != 0:
          print("false")
     else :
          if Y % 4 == 0:
               print("true")
          else : 
               print("false") 
else:
     print("true")
     