n=int(input())
a=0
b=1
sum=0
i=1
while i<=n:
    sum=a+b
    a=b
    b=sum
    i=i+1

print(a)