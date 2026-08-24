class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()

        cf = 0
        ce = nums[0]
        res = []
        i = 0

        while i < len(nums):
            if nums[i] == ce:
                cf += 1
                i += 1
            else:
                if cf > len(nums) // 3:
                    res.append(ce)

                ce = nums[i]
                cf = 0

        if cf > len(nums) // 3:
            res.append(ce)

        return res