li=list(map(int,input().split()))
max=li[0]
for num in li:
    if num>max:
        max=num
print(max)
