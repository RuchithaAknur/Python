from functools import reduce
nums = [1, 2, 3, 4, 5, 6]
even=reduce(lambda a,b:a+b if b%2==0 else a,nums,0)
print(even)

from functools import reduce
dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
result=reduce(lambda a,b:{**a,**b},dicts)
print(result)

from functools import reduce
words=["cat", "elephant", "dog", "tiger"]
longest=reduce(lambda a,b:a if len(a)>len(b) else b,words)
print(longest)

from functools import reduce
n=5
fact=reduce(lambda a,b:a*b,range(1,n+1))
print(fact)

from functools import reduce
digits = [9, 2, 6, 5]
num=reduce(lambda a,b:a*10+b,digits)
print(num)
