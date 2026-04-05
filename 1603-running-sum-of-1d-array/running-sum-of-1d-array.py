class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ps=[]
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            ps.append(c)
        return ps
        