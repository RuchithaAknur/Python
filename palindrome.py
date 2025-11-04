##Palindrome number
class Solution:
    def isPalindrome(self, n):
        p=str(n)
        a=p[::-1]
        if a==str(n):
            return True
        else:
            return False

