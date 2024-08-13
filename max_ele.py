arr=[12,6,0,3,45,11]
max=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
print("Maximum element: ",max)
