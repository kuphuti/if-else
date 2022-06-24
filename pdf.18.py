phy=int(input("enter phy"))
che=int(input("enter che"))
bio=int(input("enter bio"))
math=int(input("enter math"))
com=int(input("enter com"))
total=phy+che+bio+math+com
per=total/500*100
if per>90:
    print("grade A")
elif per>80:
    print("grade B")    
elif per>70 :
    print("grade C")   
elif per>60:
    print("grade E")    
elif per<40:
    print("grade F")
else:
    print("none")    