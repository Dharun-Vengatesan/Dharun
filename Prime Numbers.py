x=int(input("Enter Limit:"))
for num in range(x+1):
    i=2
    while i<num:
        if num%i==0:
            break
        i+=1
    else:
        print(num,"is a prime number")
