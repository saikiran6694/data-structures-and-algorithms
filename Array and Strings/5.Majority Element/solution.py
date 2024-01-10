class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = {}

        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        
        for i in res:
            if res[i] > n // 2:
                return i
                