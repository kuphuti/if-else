salary=int(input("enter salary"))
year_service=int(input("enter year"))
if year_service>5:
    b=salary/100*5
    total_salary=salary+b
    print(total_salary)
else:
    print("no bonus")    
