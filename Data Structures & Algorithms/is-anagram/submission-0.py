class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1=defaultdict(int)
        d2=defaultdict(int)
        for w in s:
            d1[w]+=1
        for w in t:
            d2[w]+=1
        if d1==d2:
            return True
        else:
            return False