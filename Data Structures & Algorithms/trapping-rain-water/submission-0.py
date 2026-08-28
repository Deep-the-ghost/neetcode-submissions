class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = 0
        maxright = 0
        left = []
        right = [0]*len(height)
        mins = [0]*len(height)
        water = 0
        for num in height:
            left.append(maxleft)
            if num >maxleft:
                maxleft = num 
        for i in range(len(height)-1,-1,-1):
            right[i] = maxright
            if height[i] > maxright:
                maxright = height[i]
            mins[i] = min(left[i],right[i])
            if height[i] < mins[i]:
                water += mins[i]-height[i]
        return water        