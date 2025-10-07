str1 = input()
sentence=list(str1)
sentence[1]='a'
sentence[-2] = 'a'
print(''.join(sentence))    
