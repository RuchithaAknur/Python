l=[2,3,4,5,6,7,8]
primes=[]
add=0
for i in l: 
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                add+=i
        else:
            pass
print(add)
