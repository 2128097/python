n=int(input())
sum1=0
sum2=0

while n!=0:
    rem=n%10
    if rem%2==0:
        sum1=sum1+rem
    else:
        sum2=sum2+rem
    n=n//10

print(sum1," ",sum2)