print("----------ADD OR EVEN----------")

ans="yes"
while ans=="yes":
    num=int(input("Enter a Number:"))
    if num%2==0:
        print("EVEN NUMBER")
    else:
        print("ODD NUMBER")
    ans=input("Want To Enter  More(yes/no):")
