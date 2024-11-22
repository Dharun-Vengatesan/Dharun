print("Armstrong Number")
sum=0
n=int(input("Enter the number:"))
x=n
while n>=0:
    r=n%10
    n=n//10
    sum=sum+(r**3)
    if sum==x:
        print(x,"it is a armstrong number")
    else:
        print(x,"not an armstrong number")
