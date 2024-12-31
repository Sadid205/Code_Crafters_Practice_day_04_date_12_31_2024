def TShape2(X):
    N = X
    K = X-1
    M = 1
    while N>0:
        for i in range(0,K):
            print(" ",end="")
        for j in range(0,M):
            print("*",end="")
        print()
        K-=1
        M+=2
        N-=1
        
X = int(input(""))
TShape2(X)