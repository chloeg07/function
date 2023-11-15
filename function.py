def someNum():
    x = input("enter a number: ")
    x = int(x)
    return x
Num = someNum()

def myCount(value):
    for i in range(1, value+1):
        print(i)
myCount(Num)
    