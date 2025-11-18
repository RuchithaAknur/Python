n=int(input("enter a number:"))
if n&1==0:
    print("even")
else:
    print("odd")

n=int(input("enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
    if n>i:
        print(i,end="*")
print(n,"=",fact)
    
str1=input("enter a string:")
result=""
rev=""
for i in str1:
    if i!=" ":
        result=i+result
    else:
        rev=rev+""+result
        result=" "
rev=rev+" "+result
print(rev)

n="123456"
e=0
o=0
for i in range(1,len(n)+1,2):
    e=e+int(i)
for j in range(0,len(n)+1,2):
    o=o+int(j)
print(e-o)

num=[2,3,6,9,23,14]
max_num=num[0]
min_num=num[0]
for i in num[1:]:
    if i>max_num:
        max_num=i
    if i<min_num:
        min_num=i
print("maximum:",max_num)
print("minimum:",min_num)

num=[int(num) for num  in input().split()]
for i in range(0,len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
print(num) 

n=int(input("enter a number:"))
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("not a prime")
            break
    else:
        print("prime")

else:
    print("invalid")


n=int(input("enter a number:"))
a,b=0,1
for i in range(0,n):
    print(a,end=" ")
    a,b=b,a+b

n=int(input("enter a number:"))
a,b=0,1
i=1
while i<=n:
    a,b=b,a+b
    print(a)
    i+=1
    
num=[12,34,56,67,78,89]
max_num=num[0]
sec_max=num[0]
min_num=num[0]
sec_min=num[0]
for i in num[1:]:
    if i>max_num:
        sec_max=max_num
        max_num=i
    elif i>sec_max and i<max_num:
        sec_max=i
    if i<min_num:
        sec_min=min_num
        min_num=i
    elif i<sec_min and i>min_num:
        sec_min=i
print(sec_max)
print(sec_min

n=int(input("enter a number:"))
a,b=0,1
i=1
while i<=n:
    print(a)
    a,b=b,a+b
    i+=1

str1=input("enter a string:")
count=0
for i in str1:
    if i in "aeiou":
        count+=1
print(count)

n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n1=n1^n2
n2=n1^n2
n1=n1^n2
print(n1,n2)

l=[12,34,56,78]
l1=[34,2,56,9]
for i in l:
    for j in l1:
        if i==j:
            print(i,end=" ")


l=[1,2,3,4,5,1,2]
temp=[]
c=0
for i in l:
    if i not in temp:
        temp=temp+[i]
print(temp)
for i in temp:
    c=0
    for j in l:
        if i==j:
            c+=1
    print(f"{i}:{c}")


str1="ruchitha"
res={}
for i in str1:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
print(res)


n=int(input("enter a number:"))
power=len(str(n))
digit=0
temp=n
while temp>0:
    rem=temp%10
    digit=digit+rem**power
    temp//=10
print(digit)
if digit==n:
    print("armstrong number")
else:
    print("not armstrong number")


num=[12,34,56,67,78,89]
max_num=num[0]
sec_max=num[0]
min_num=num[0]
sec_min=num[0]
for i in num[1:]:
    if i>max_num:
        sec_max=max_num
        max_num=i
    elif i>sec_max and i<max_num:
        sec_max=i
    if i<min_num:
        sec_min=min_num
        min_num=i
    elif i<sec_min and i>min_num:
        sec_min=i
print(sec_max)
print(sec_min)

a=10
b=30
while b:
    a,b=b,a%b
print(a)

a=10
b=30
max_num=max(a,b)
while True:
    if max_num%a==0 and max_num%b==0:
        print(max_num)
        break
    max_num+=1

n=[1,2,93,84,55]
for i in n[::-1]:
    print(i,end=" ")


str1="ruchitha"
count=0
for i in str1:
    count+=1
print(count)

n=int(input("enter a number:"))
binary=""
if n==0:
    binary="0"
else:
    while n>0:
        binary=str(n%2)+binary
        n//=2
print(binary)

l=[23,4,5,6]
add=0
for i in l:
    add+=i
print(add)

d1={"a":1, "b":3}
d2={"c":9, "d":5}
merged={**d1,**d2}
d1.update(d2)
print(d1)

d={"a":1,"b":2,"c":7}
key=input("enter a key:")
if key in d:
    print(f"{key} exist")
else:
    print(f"{key} not exist")


class human:
    def eat(self):
        print("eating")
    def sleep(self):
        print("sleeping")
    def drink(self):
        print("drinking")
a1=human()
a1.sleep()
    
    
class parent1:
    def display(self):
        print("this is a parent1")
class parent2:
    def show(self):
        print("this is a parent2")
class child(parent1,parent2):
    def show_details(self):
        print("this is a child")
a1=child()
a1.show()

x=((lambda a,b:a+b)(10,20))
print(x)

l=[2,3,4,5,6]
def even(l):
    for i in l:
        if i%2==0:
            
  
s="ruchitha_ru_thika"
for i in s:
    if i=="_":
        continue
    print(i,end="")
        

num=[10,20,30,40]
print(num[-3:-1])

num=[1,2,3,4]
print(sum(num[1:3]))

d={"a":1,"b":2}
d2={"b":4,"c":4}
d2.update["d"]
print(d)


n=[1,2,3,4]
x=list(map(lambda a:a**2,n))
print(x)

words=["python","is","fun"]
x=list(map(lambda a:a.upper(),words))
print(x)

n=[10,20,30,40]
x=list(map(lambda a:str(a),n))
print(x)

words=["apple","banana","cherry"]
x=list(map(len,words))
print(x)

l1=[1,2,3]
l2=[4,5,6]
x=list(map(lambda a,b:a+b,l1,l2))
print(x)

class calculator:
    def add(self,a,b):
        print("sum:",a+b)
    def sub(self,a,b):
        print("sub:",a-b)
a1=calculator()
a1.add(5,10)
a1.sub(10,20)
