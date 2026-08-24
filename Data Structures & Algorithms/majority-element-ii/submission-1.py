class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res=[]
        for v in count:
            if count[v]>len(nums)//3:
                res.append(v)
        return res
