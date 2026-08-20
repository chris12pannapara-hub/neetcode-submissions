class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set(nums)
        # longest , length = 0 , 1

        # for n in numSet:
        #     if (n-1) not in numSet:
        #         while(n + length) in numSet:
        #             length += 1
        #         longest = max(length, longest)

        # return longest

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest       