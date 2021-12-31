a,b,c=map(int,input("enter three numbers ").split())
if a>b and a>c:
    print(str(a) + " is largest number")
elif b>a and b>c:
    print(str(b) + " is largest number")
else:
    print(str(c) + " is largest number")
