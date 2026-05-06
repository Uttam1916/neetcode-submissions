class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater=0
        currwater=0
        l,r=0,len(heights)-1
        while l<r:
            currwater=(r-l)*min(heights[l],heights[r])
            maxwater=max(currwater,maxwater)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return maxwater