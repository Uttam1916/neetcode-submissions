class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fr=defaultdict(int)
        bk=defaultdict(int)
        l=len(nums)
        for i in range(0,l):
            if i==0:
                fr[i]=nums[i]
            else:
                fr[i]=fr[i-1]*nums[i]
        for i in range(l-1,-1,-1):
            if i==l-1:
                bk[i]=nums[i]
            else:
                bk[i]=bk[i+1]*nums[i]
        res=[bk[1]]
        print(fr)
        print(bk)
        for i in range(1,l-1):
            res.append(fr[i-1]*bk[i+1])
        res.append(fr[l-2])
        return res