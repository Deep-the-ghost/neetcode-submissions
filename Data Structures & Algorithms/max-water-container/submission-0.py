class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(heights)-1
        while i < j:
            maxArea = max((min(heights[i],heights[j])*(j-i)),maxArea)
            if (min(heights[i+1],heights[j])*(j-i+1)) > maxArea:
                i += 1
            elif (min(heights[i],heights[j-1])*(j-i-1)) > maxArea:
                j -= 1
            else:
                j -= 1
        return maxArea                 

