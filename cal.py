num1=float(input("enter the first number: "))
operator= input("enter the operator: ")
num2=float(input("enter the second number: "))
if operator=="+":
    print("your answer is: ",num1+num2);
elif operator=="-":
    print("your answer is:", num1-num2);
elif operator=="*":
    print("your answer is: ", num1*num2);
elif operator=="/":
    if num2 !=0:
        print("your answer is: ",num1/num2);
    else:
        print("numbers are not divisble by 0.");
else:
    print("ivalid operator.")