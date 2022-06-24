x=int(input("enter x"))
y=int(input("enter y"))
z=int(input("enter z"))
if x==y==z:
    print("equelateral")
elif x!=y and y!=z and z!=x:
    print("scalene")
else:
    print("isosceles")        