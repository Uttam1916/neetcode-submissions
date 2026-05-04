class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present=dict()
        for i in range(len(nums)):
            if target-nums[i] in present:
                return [present[target-nums[i]],i]
            else:
                present[nums[i]]=i
