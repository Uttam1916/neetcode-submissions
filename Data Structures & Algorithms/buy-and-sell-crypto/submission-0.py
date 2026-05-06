class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        for p in prices:
            maxprofit=max(maxprofit,p-minprice)
            minprice=min(minprice,p)
        return maxprofit