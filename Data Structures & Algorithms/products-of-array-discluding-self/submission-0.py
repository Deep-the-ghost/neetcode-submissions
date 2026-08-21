class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        product = 1

        # Left side
        for i in range(len(nums)):
            answer[i] = product
            product *= nums[i]

        product = 1

        # Right side
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer