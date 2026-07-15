class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = 0

        for x in nums:
            curr += x
            best = max(best, curr)

            if curr < 0:
                curr = 0

        return best