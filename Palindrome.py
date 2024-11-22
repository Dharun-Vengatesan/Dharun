print("Palindrome")
def isPal(s):
    return s==s[::-1]
s=input("Enter the Pharse:")
ans= isPal(s)
if ans:
    print(s,"it is a palindrome")
else:
    print("Not a Palindrome")
