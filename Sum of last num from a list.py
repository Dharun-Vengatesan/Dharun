L=[5,15,92,99,25,12]
sum=0
x=len(L)
for i in range(0,x):
    if type(L[i])==int:
        if L[i]%10==5:
            sum+=L[i]
print(sum)
