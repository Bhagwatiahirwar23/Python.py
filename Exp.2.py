i = int(input("Enter a Number"))
x = i
rev = 0
while(i>0):
    rev = rev*10 + i%10
    i = i//10
if(x == rev):
    print("Number is palindrome")
else:
    print("Number is not palindron")