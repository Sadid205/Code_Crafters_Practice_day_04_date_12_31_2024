def Shape3(X):
    N = X
    K = X*2
    M = N-1
    S = 0
    L = 1
    R = (2*N)-1
    for i in range(0,K):
        if i<N:
            for j in range(0,M):
                print(" ",end="")
            for k in range(0,L):
                print("*",end="")
            print()
            M-=1
            L+=2
            K-=1
        else:
            for l in range(0,S):
                print(" ",end="")
            for m in range(0,R):
                print("*",end="")
            print()
            S+=1
            R-=2
            K-=1

X = int(input(""))
Shape3(X)