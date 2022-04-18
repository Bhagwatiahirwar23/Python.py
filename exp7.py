#write a program to print fibonocci series using recursion
number = int(input("how many terms"))
n1,n2 = 0,1
count = 0
if number <= 0:
    print("please enter a positive integer")
elif number == 1:
    print("fibonacci seqence upto",number,":")
    print(n1)
else:
    print("fibonacci sqenence:")
    while count < number:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1