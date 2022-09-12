n = int(input("Enter a number"))
sum = 0
cpN = n
Order = len(str(n))
while (n > 0):
    a = n % 10
    sum += a ** Order
    n = n // 10
if sum == cpN:
    print("Yes, it is an Armstrong Number")
else:
    print("No, it is not an Armstrong Number")




