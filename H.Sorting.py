def Sorting(size,array):
    
    for i in range(0,size-1):
        for j in range(i+1,size):
            if array[i]>array[j]:
                temp = array[i]
                array[i]=array[j]
                array[j]=temp
    for num in array:
        print(num,end=" ")



X = int(input(""))
Y = input("")
Y_split = Y.split()
array = [int(num) for num in Y_split]
Sorting(X,array)