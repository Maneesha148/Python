n=int(input("Enter the length of the series: "))
l1=0
l2=1
print(l1)
print(l2)
i=0
while(i<n-2):
    l3=l1+l2
    print(l3)
    l1=l2
    l2=l3
    i=i+1
