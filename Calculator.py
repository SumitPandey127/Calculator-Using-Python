
print("--WELCOME TO THE0 CALCULATOR--")
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

while True:
    operation = int(input("Enter \n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Exit/Stop\n"))

    if operation==1:
        num3=num1+num2
        print(f"Addition of {num1} and {num2} = {num3}")
    elif operation==2:
        num4=num1-num2
        print(f"Subtraction of {num1} and {num2} = {num4}")
    
    elif operation==3:
        num5=num1*num2
        print(f"Multiplication of {num1} and {num2} = {num5}")
    
    elif operation==4:
        num6=num1//num2
        print(f"Division of {num1} and {num2} = {num6}")
    
    elif operation == 5:
        print("Closing the program....")
        break
    else:
        print("Invalid Input. Please enter a number from 1 to 5.")
