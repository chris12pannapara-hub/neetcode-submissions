class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        for i in range(len(s)):
            res += self.helps(s, i, i)
            res += self.helps(s, i, i+1)
        return res

    

    def helps(self, s, l ,r):
        res = 0
        while l>=0 and r <=len(s)-1 and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res