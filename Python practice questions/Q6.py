# Simple Calculator
# Ask for two numbers and an operator (+, -, *, /) and perform the calculation using if/elif/else.


a=input("Select the optuion (+, -, *, /): ")

if a=="+":
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))

    b=num1+num2
    print(b)

elif a=="-":
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))

    b=num1-num2
    print(b)
elif a=="*":
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))

    b=num1*num2
    print(b)
elif a=="/":
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))

    b=num1/num2
    print(b)
    
