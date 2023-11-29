n = int(input("Enter a decimal number:"))
 
bin = ''
rem = 0 

while n > 0:
    rem = n%2
    n = n//2
    
    bin = str(rem)+bin
print(bin)