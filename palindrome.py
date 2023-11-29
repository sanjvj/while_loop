n = int(input("Enter the number to be checked: "))
m = n
rev = 0 

while n>0:
    r=n%10
    n=n//10

    rev=rev*10+r
print("Reverse of the number is:",rev)

if m==rev:
    print("It is palindrome")
else:
    print("Not a palindrome number")