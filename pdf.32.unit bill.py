unit=int(input("enter unit"))
if unit<=100:
    print("no change")
elif unit>100 and unit<200:
    bill=(unit-100)*5
    print(bill)
elif unit>100:
    bill=(unit-150)*10
    print(bill) 
else:
    print("no bill")      