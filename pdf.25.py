working_days=int(input("enter working days"))
attendence=int(input("enter attendence"))
per=attendence/working_days*100
if per<75:
    print("not allowed")
else:
    print("allowed")    
