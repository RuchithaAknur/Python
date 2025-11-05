def dup_ele(l):
    temp=[]
    dup=[]
    for i in l:
        if i not in temp:
            temp.append(i)
        else:
            dup.append(i)
    return dup
l=[10,5,15,5,15,80]
print(dup_ele(l))



def largest_sum(l):
    max_num=l[0]
    for i in l:
        if i>max_num:
            max_num=i
    add=0
    temp=max_num
    while temp>0:
        rem=temp%10
        add+=rem
        temp//=10
    return add
l= [100, 150, 200, 180]
print(largest_sum(l))
