1=[23,45,78,98,12,67]
max_num=sec_max=l1[0]
min_num=sec_min=l1[0]
for i in l1[1:]:
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
print("second maximum:",sec_max)
print("second minimum:",sec_min)
