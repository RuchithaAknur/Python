n=[12,34,57,33,5,7,9]
primes=[]
for index,num in enumerate(n):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(f"prime{num} found at index {index}")
