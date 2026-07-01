class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f,s=0,0
        n,m=len(word1),len(word2)
        res=""
        while f<n and s<m:
            res= res+ word1[f] + word2[s]
            f+=1
            s+=1
        if f<n:
            res+=word1[f:]
        else:
            res+=word2[s:]
        return res