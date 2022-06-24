c_p=int(input("enter num"))
if c_p>100000:
    tax=c_p*15/100
    print(tax)
elif c_p>50000 and c_p<=10000:
    tax=c_p*10/100
    print(tax) 
elif c_p<=50000:
    tax=c_p*5/100
    print(tax) 
else:
    print("not tax")          