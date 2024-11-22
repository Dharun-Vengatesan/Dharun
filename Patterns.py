print("patterns")
print("1.Star pattern\n2.Number in a row\n3.Increasing number")
ch=int(input("Enter Your Choice"))
rows=int(input("Enter the no.of rows"))
if ch==1:
    for i in range(0,rows+1):
        for j in range(0,i):
            print("*",end=" ")
        print(" ")
if ch==2:
    for i in range(0,rows+1):
        for j in range(0,i):
            print(i,end=" ")
        print(" ")
if ch==3:
    for i in range(0,rows+2):
        for j in range(1,i):
            print(i,end=" ")
        print(" ")
