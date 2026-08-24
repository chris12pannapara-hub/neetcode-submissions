class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maxAmt = 0
        # for i in range(len(heights)):
        #     j = len(heights) - 1
        #     dis = j - i
        #     area = dis * min(heights[i], heights[j])
        #     maxAmt = max(area , maxAmt)
        #     j -= 1
        
        # return maxAmt

        maxAmt = 0

        l , r = 0 , len(heights) - 1

        while l < r:
            area = ( r - l ) * min(heights[l], heights[r])
            maxAmt = max(area , maxAmt)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxAmt


        