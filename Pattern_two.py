n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or i==n-1 or (j==0 and i>=n//2) or (i<=n//2 and j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
