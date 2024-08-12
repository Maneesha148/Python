arr=[10,12,24,3,7,234]
print("To find the maximum element of an array...")
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("Maximum Element is:",max)
