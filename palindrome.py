num=int(input())
rev=str(num)[::-1]
rev=int(rev)
if rev==num:
    print("Palindrome")
else:
    print("Not Palindrome")
