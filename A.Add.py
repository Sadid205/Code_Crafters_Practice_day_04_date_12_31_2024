def Add(array):
    sum = 0
    for num in array:
        sum+=num
    print(sum)


x = input("")
x_split = x.split()
x_array = [int(num) for num in x_split]
Add(x_array)