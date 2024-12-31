def PShape1(X):
    while X>0:
        temp=X
        while temp>0:
            print("*",end="")
            temp-=1
        print()
        X-=1
X  = int(input(""))
PShape1(X)