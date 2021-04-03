print("Please enter the value of row")
r=int(input())
print("Please enter the value of column")
c=int(input())

row=1
while row <=r:
      column=1
      while column <=c:
           print("*", end="")
           column += 1
      row += 1
      print("")
