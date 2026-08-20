class Solution:
    def isPalindrome(self, s: str) -> bool:
        revers = ""
        for i in s:
            if i.isalnum():
                revers += i.lower()  
        return revers == revers[::-1]
        