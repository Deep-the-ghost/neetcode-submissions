class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        sorted_seen = sorted(seen.items(), key=lambda x: x[-1], reverse = True)            
        for i in range(k):
            res.append(sorted_seen[i][0])
        return res    