class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # res = [];
        # for i in nums:
        #     if nums[i] == res:
        #         return True
        #     else:
        #         return False


        res = set()
        for i in nums:
            if i in res:
                return True
            res.add(i)
        return False
        
        