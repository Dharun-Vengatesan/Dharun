n=int(input("Enter the limit value:"))
a=0
b=1
c=1
print("Fibonacci Series\n")
print(a,b,end=" ")
while(c<=n):
    print(c,end=" ")
    a=b
    b=c
    c=a+b
