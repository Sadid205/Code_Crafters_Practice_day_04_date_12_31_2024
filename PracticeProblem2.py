def Traingle(X):
    K = (X*2)-1
    L = 0
    N = X
    while N>0:
        for i in range(0,L):
            print(" ",end="")
        for j in range(0,K):
            print("*",end="")
        print()
        L+=1
        K-=2
        N-=1




X = int(input(""))
Traingle(X)