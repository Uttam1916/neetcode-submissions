class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        res = []
        i = 0
        n=len(nums)
        while i <n:
            j=i+1
            while j<n and nums[j]==nums[i]:
                j+=1
            if (j-i)>n//3:
                res.append(nums[i])
            i=j

        return res