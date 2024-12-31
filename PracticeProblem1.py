def Traingle(X):
    K=X-1
    L=1
    N = X
    while N>0:
        for i in range(0,K):
            print(" ",end="")
        for j in range(0,L):
            print("*",end="")
        print()
        L+=1
        K-=1
        N-=1


X = int(input(""))
Traingle(X)