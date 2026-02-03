# A basic simple calculator programs for 2 numbers

operator=input("enter the operation you want to perform(+/-/*//) : ")
num1=float(input("enter number 1 : "))
num2= float(input("enter number 2 : "))

if operator=="+":
    result=num1+num2
    print(round(result,3))
elif operator=="-":
    result=num1-num2
    print(round(result,3))
elif operator=="*":
    result=num1*num2
    print(round(result,3))
elif operator=="/":
    result=num1/num2
    print(round(result,3))
else:
    print(f"The {operator} you have entered is not valid")            
        