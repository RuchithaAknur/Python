n=int(input("enter a number:"))
a,b=0,1
found=False
for i in range(n+1):
    if a==n:
        found=True
        break
    a,b=b,a+b
if found:
    print("true")
else:
    print("false")


def is_fibo(l):
    a,b=0,1
    while a<=l:
        if a==l:
            return True
        a,b=b,a+b
    return False
n=list(map(int,input("enter numbers:").split()))
add=0
for i in n:
    if is_fibo(i):
        add+=i       
print(add)
