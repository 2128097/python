a=int(input())
while a!=6:
    if a==1:
        c=int(input())
        d=int(input())
        sum=c+d
        print(sum)
    elif a==2:
        c=int(input())
        d=int(input())
        sub=c-d
        print(sub)
    elif a==3:
        c=int(input())
        d=int(input())
        mult=c*d
        print(mult)
    elif  a==4:
        c=int(input())
        d=int(input())
        div=int(c/d)
        print(div)
    elif a==5 :
        c=int(input())
        d=int(input())
        mod=int(c%d)
        print(mod)
    elif a<1 or a>6:
        print("Invalid Operation")
    a=int(input())  