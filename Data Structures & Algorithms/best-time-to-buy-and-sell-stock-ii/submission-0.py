class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=prices[0]
        prof=0
        for v in prices:
            if v<curr:
                curr=v
                continue
            if v>curr:
                prof+=v-curr
                curr=v
        return prof

            