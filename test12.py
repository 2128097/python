n=int(input())
rev_num=0

while n!=0:
    rem=n%10
    rev_num=rev_num*10+rem
    n=n//10

print(rev_num)