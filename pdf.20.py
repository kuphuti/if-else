unit_change=int(input("enter unit_change"))
if unit_change>=1 and unit_change<=50:
    total_bill=unit_change*0.50+20/100
    print("total bill=",total_bill)
elif unit_change>=51 and unit_change<=151:
    total_bill=unit_change*0.75+20/100
    print("total_bill=",total_bill)    
elif unit_change>=152 and unit_change<=251:
    total_bill=unit_change*1.20+20/100
    print("total_bill=",total_bill)   
elif unit_change>250:
    total_bill=unit_change*1.50+20/100
    print("total_bill=",total_bill)  
else:
    print("not generate")     