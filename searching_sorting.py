#selection sort
# def sorting(n):
#     for i in range(len(n)-1):
#         for j in range(i+1,len(n)):
#           if n[i]>n[j]:
#                 n[i],n[j]=n[j],n[i]
#     return n
# n=[71,5,4,3,8,1,9,2]
# print(sorting(n))

#linear search
# def linear_search(n):
#     for i in range(len(n)):
#         if n[i]==ele:
#             return i
#     return False
# n=[12,34,56,78,90]
# ele=int(input("enter a element:"))
# print(linear_search(n))


#binary search
# def binary_search(n,ele):
#     low=0
#     high=len(n)-1
#     while low<=high:
#         mid=(low+high)//2
#         if n[mid]==ele:
#             return mid
#         elif n[mid]>ele:
#             return mid-1
#         elif n[mid]<ele:
#             return mid+1
#     return -1
# n=[12,34,56,78,90,22,33,44]
# ele=int(input("enter a element:"))
# print(binary_search(n,ele))


