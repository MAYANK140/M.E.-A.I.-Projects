n=int(input("Enter the number of digits you want to see in the Fibonacci series"))
a,b,c=0,1,1
for i in range(n):
    print(c, "\n")
    c=a+b
    a=b
    b=c
