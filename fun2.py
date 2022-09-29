def getsalary():
    val=int(input('Enter amount'))
    fine=.09
    sal=val*fine
    return sal

ans=getsalary()
print("salary",ans)

final_sal=getsalary()+1000
print("salary",final_sal)

def amt():
    p=int(input('Enter principle amount'))
    r=int(input('Enter rate'))
    t=int(input('Enter time'))
    si=(p*r*t)/100
    amt=si+p
    return amt,si

ans=amt()
print(f'the Anount will be {amt} on Simple interest {si}')
#or
print(f'the Amount will be {amt()[0]}')