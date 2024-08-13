arr=[2,4,2,6,4,6,8,2,5]
seen=set()
unique=[]
for i in arr:
    if i not in seen:
        unique.append(i)
        seen.add(i)
print(unique)
