class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if len(strs)==0:
            return ""
        minlen= min(len(s) for s in strs)
        for i in range(minlen):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    return strs[0][:i]
        mins=strs[0]
        for s in strs:
            if len(s)<len(mins):
                mins=s
        return mins