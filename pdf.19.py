b_s=int(input("enter salary"))
if b_s<=10000:
        hra=b_s*20/100
        da=b_s*80/100
        gross_salary=b_s+hra+da
        print(gross_salary)
elif b_s<=20000:
        hra=b_s*25/100
        da=b_s*90/100
        gross_salary =b_s+hra+da 
        print(gross_salary)     
elif b_s>2000:
        hra=b_s*30/100
        da=b_s*95/100
        gross_salary=b_s+hra+da
        print(gross_salary) 
else:
        print("none")               