Mode = int(input('''For Addition Press 1
For Subtraction Press 2
For Product Press 3
For Division Press 4'''))
Num1 = int(input("Enter First Number."))
Num2 = int(input("Enter Second Number"))
if (Mode==1):
    print("Addition is ", Num1 + Num2)
elif (Mode==2):
    print("Subtraction is ", Num1 - Num2)
elif (Mode == 3):
    print("Product is ", Num1 * Num2)
elif (Mode == 4):
    print("Division is ", Num1 / Num2)
else:
    printf("Invalid Entry")
