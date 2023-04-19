print("------------LETS CHECK WETHER THE GIVE STRING IS PALINDROM OR NOT------------")
ans="yes"
while ans=="yes":
    p=input("Enter The Value To Be Checked:")
    if p==p[::-1]:
        print("String Is Palindrom")
    else:
        print("It Is Not a Palindrom")
    ans=input("Want To More:")
