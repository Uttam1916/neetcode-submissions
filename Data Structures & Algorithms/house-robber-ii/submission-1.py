class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(nums):
            r1,r2=0,0
            for n in nums:
                temp=max(r1+n,r2)
                r1=r2
                r2=temp
            return r2
        return max(helper(nums[:len(nums)-1]),helper(nums[1:]))