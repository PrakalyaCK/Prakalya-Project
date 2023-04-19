print("select anoperation to be performed")
print("ADD")
print("SUBTRACT")
print("MULTIPLY")
print("DIVIDE")
print("POWER")
print("REMAINDER")

ans="yes"

while ans=="yes":
    operation=input("Enter Your Choice:")
    num1=int(input("Enter 1st Number:"))
    num2=int(input("Enter 2nd Number:"))
    if operation.lower()=="add":
        print(num1+num2)
    elif operation.lower()=="subtract":
        print(num1-num2)
    elif operation.lower()=="multiply":
        print(num1*nuM2)
    elif operation.lower()=="divide":
        print(num1/num2)
    else:
        print(num1**num2)
    ans=input("Want To Perform More(yes/no):")
    
    
    
