l1=[1,2,3]
for i in l1:
    print(i,end=" ")

l1=[10,20,30,40]
print(l1[0])
print(l1[-1])

l1=[1,2,3]
l1.append(4)
print(l1)

l1=[1,2,3,4]
item=3
temp=[]
for i in l1:
    if i!=item:
        temp.append(i)
print(temp)

l1=[10,20,30]
x=len(l1)
print(x)

l1=[2,4,5]
add=0
for i in l1:
    add+=i
print(add)

l1=[2,3,4,5,6,7,8,9]
even=[]
for i in l1:
    if i%2==0:
        even.append(i)
print(even)

l1=[2,3,4]
x=l1[:]
print(x)

l=[2,56,7,9,90,23]
max_num=l[0]
min_num=l[0]
for i in l:
    if i>max_num:
        max_num=i
    if i<min_num:
        min_num=i
print(max_num)
print(min_num)


l=[2,3,4,5]
l1=[]
for i in range(len(l)-1,-1,-1):
    l1+=[l[i]]
print(l1)


l1=[23,45,67,89]
sec_max=l1[0]
max_num=l1[0]
for i in l1:
    if i>max_num:
        sec_max=max_num
        max_num=i
    elif i>sec_max and i<max_num:
        sec_max=i
print(sec_max)


l1=[1,2,3,1,2]
temp=[]
for i in l1:
    if i not in temp:
        temp.append(i)
print(temp)

l=[1,2,2,3,1,4,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)


l=[5,2,8,1,3]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

l1=[1,2,3,4]
l2=[3,4,5,6]
common=[]
for i in l1:
    if i in l2 and i not in common:
        common.append(i)
print(common)
