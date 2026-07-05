class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def comb(i,curr,li):
            if curr==target:
                res.append(li.copy())
                return
            if curr>target or i>=len(nums):
                return
            
            li.append(nums[i])
            comb(i,curr+nums[i],li)
            li.pop()
            comb(i+1,curr,li)

        comb(0,0,[])
        return res