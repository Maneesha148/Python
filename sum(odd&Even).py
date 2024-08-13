arr=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(len(arr)):
    if arr[i]%2==0:
        sum1+=arr[i]
    else:
        sum2+=arr[i]
print(sum1,"",sum2)
