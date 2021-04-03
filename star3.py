print("Please Enter the Value of row")
row=int(input())

a = row
b = 0

for i in range(a, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\r')