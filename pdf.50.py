month=input("enter month")
day=input("enter day")
if month==("dec,jan,feb"):
    if day=="31,28/29":
        print("winter")
elif month in ("june,july"):
    if day=="30,31":
        print("summer")
else:
    print("not found")        
        

