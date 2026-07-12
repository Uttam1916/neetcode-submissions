class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r= max(weights),sum(weights)
        def can(c):
            d,cap=1,c
            for w in weights:
                if cap-w<0:
                    cap=c
                    d+=1
                    if d>days:
                        return False
                cap-=w
            return True
        while l<r:
            c=(l+r)//2
            if can(c):
                r=c
            else:
                l=c+1
        return r