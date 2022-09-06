email=input('enter ur email: ')
if '@' in email:
    if len(email)>=11:
        if '.com' in email or 'org' in email:
            print("valid email")
        else:
            print("invalid domain")
    else:
        print("length of email is not valid") 
else:
    print('email does not have"@"') 