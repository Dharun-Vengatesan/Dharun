str1=input("Enter a string:")
n=c=d=s=u=l=o=0
for ch in str1:
    if ch.isalnum():
        n+=1
        if ch.isupper():
            u+=1
        elif ch.islower():
            l+=1
        elif ch.isalpha():
            c+=1
    if ch.isdigit():
        d+=1
    elif ch.isspace():
        s+=1
    else:
        o+=1
print("Number of Alphabers and Digits",n)
print("Number of Capital Letters",u)
print("Number of Small Letters",l)
print("Number of Digits",d)
print("Number of Spaces",s)
print("Number of other charecters",o)

