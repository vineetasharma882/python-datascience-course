email=input("enter email")
if '@' not in email:
    print('email does not have @')
elif len(email) < 11:
    print('length of email is invalid')
elif '.com' not in email and '.org' not in email:
    print("invalid domain")
else:
    print("valid email")
    