A, B, C = map(int, input().split())

if A < B < C :
    print(B)
elif C < B < A:
    print(B)
elif B < A < C:
    print(A)
elif C < A < B :
    print(A)
elif A < C < B :
    print(C)
elif B < C < A:
    print(C)