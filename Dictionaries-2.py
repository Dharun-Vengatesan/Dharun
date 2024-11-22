classxi=dict()
n=int(input("Enter the total no. of sections present in class xi:"))
i=1
while i<=n:
    a=input("Enter the Section:")
    b=input("Enter the Stream name:")
    classxi[a]=b
    i=i+1
print("Class",'\t',"Section",'\t',"Stream Name")
for i in classxi:
    print("XI",'\t',i,'\t',classxi[i])
    
