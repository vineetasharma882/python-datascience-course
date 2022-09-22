Salary = float(input("Enter Employee Salary:"))


if Salary > 100000:
    da=(Salary*3.5)/100
    hra=(Salary*9.1)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary)

elif Salary > 80000 or Salary <= 100000:
    da=(Salary*3.2)/100
    hra=(Salary*9.0)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary)    

elif Salary > 60000 or Salary <= 80000:
    da=(Salary*2.8)/100
    hra=(Salary*9.0)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary) 

elif Salary > 50000 or Salary <= 60000:
    da=(Salary*2.5)/100
    hra=(Salary*8.0)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary)  

elif Salary > 40000 or Salary <= 50000:
    da=(Salary*2.5)/100
    hra=(Salary*7.7)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary) 

elif Salary > 30000 or Salary <= 40000:
    da=(Salary*2.2)/100
    hra=(Salary*8.0)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary)            

elif Salary > 20000 and Salary <= 30000:
    da=(Salary*2.2)/100
    hra=(Salary*7.0)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary) 

elif Salary > 10000 and Salary <= 20000:
    da=(Salary*2.2)/100
    hra=(Salary*6.0)/100
    Gross_salary = Salary+da+hra
    print("Salary Of Employee:",Gross_salary) 

else:
    print("Wrong information entered.")