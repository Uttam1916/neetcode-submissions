class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        k=0
        for i in range(3):
            c= count[i]

            while c>0:
                nums[k]=i
                k+=1
                c-=1
