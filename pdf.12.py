month=input("enter")
if month=="jan" or month=="mar" or month=="july" or month=="may" or month=="oct" or month=="dec":
    print("31 days")
elif month=="april" or month=="june" or month=="sept" or month=="nov":
    print("30 days") 
else:
    print("28/29 days")    
