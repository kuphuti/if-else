a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a>b and a>c:
    print("a is oldest")
elif b>c and c>a:
    print("b is oldest")
elif c>a and c>b:
    print("c is oldest") 
if a<b and a<c:
    print("a is youngest")
elif b<c and b<a:
    print("b is youngest")     
elif c<a and c<b:
    print("c is youngest")              
else:
    print("none of this")    