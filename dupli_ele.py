arr=[1,2,3,4,2,7]
seen=set()
for i in arr:
    if i in seen:
        duplicate=i
    seen.add(i)
print("Duplicate Element: ",duplicate)
