num=int(input())
sum=0
temp=num
while num>0:
    r=num%10
    sum=sum+r*r*r
    num=num//10
if temp==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
