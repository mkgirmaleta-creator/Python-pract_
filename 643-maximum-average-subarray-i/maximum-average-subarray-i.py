class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mt=sum(nums[:k])
        t,l,r=mt,0,k
        while r<len(nums):
            mt=mt+nums[r]-nums[l]
            r+=1
            l+=1
            t=max(t,mt)
        return t/k
        
        