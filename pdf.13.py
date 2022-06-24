amount=int(input("enter"))
if amount>0:
    a=amount//2000
    b=amount%2000
    c=b//500
    d=b%500
    e=d//200
    f=d%200
    g=f//100
    h=f%100
    i=h//50
    j=h%50
    k=j//20
    l=j%20
    m=l//10
    n=l%10
    o=n//5
    p=n%5
    print("notes of 2000=",b, "notes of 500=",d, "notes of 200=",f, "notes of 100=",h, "notes of 50=",j, "notes of 20=",l, "notes os 10=",n ,"notes os 5=",p)