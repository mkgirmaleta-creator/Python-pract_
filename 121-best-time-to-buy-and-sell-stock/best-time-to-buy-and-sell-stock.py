class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        M,m=0,float('inf')
        for i in prices:
            if i<m:
                m=i
            else:
                pfr=i-m
                M=max(M,pfr)
         
        return M


