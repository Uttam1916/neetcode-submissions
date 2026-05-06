class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        l=0
        r=0
        seen=set()
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
            else:
                while s[r] in seen and l<r:
                    seen.remove(s[l])
                    l+=1
            maxlen=max(maxlen,len(seen))
        return maxlen