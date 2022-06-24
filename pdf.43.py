age=int(input("enter age"))
sex=input("enter sex")
num_day=int(input("enter num_day"))
if age>=18 and age<=30 and sex=="m":
    amount=num_day*700
    print(amount)
elif age>=18 and age<=30 and sex=="f":
    amount=num_day*750
    print(amount)
elif age>=30 and age<=40 and sex=="m":
    amount=num_day*800
    print(amount)
elif age>=30 and age<=40 and sex=="f":
    amount=num_day*850
    print(amount)
else:
    print("no amount")    

