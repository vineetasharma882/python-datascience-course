my_dict={1:'apple',2:'ball'}
val=['Rajendra Sigh',30,0,'Accounts','Staff Officer',600000,7,]
val_dict={
    'employee':'Rajendra Singh','age':30,
    'expeience':10,
    'designation':'System Offier','salary':60000,
    'team_size':7
}
#displaying dictionary
print(val_dict)
#retreuval of values
ans=val_dict['designation']#key in sqr brackets
print(ans)
print(val_dict['salary'])
print(val_dict['expeience'])
# adding a data inside dict
val_dict['company']='Acme.inc'
print(val_dict)
from pprint import pp #(prity printng)
print(val_dict)

