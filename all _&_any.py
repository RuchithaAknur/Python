nums=[64,16,9]
def squ(nums):
    return int(nums**0.5)
res=list(map(squ,nums))
print(res)


nums=[189,10,200]
def digits(nums):
        return len(str(nums))
res=list(map(digits,nums))
print(res)
