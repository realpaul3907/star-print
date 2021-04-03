print("Please enter the value of row")
row=int(input())

for i in range(0,row):
    for j in range(0,row):
        if  j<=i:
            print("*",end='')
        else:
            print("", end="")
    print()