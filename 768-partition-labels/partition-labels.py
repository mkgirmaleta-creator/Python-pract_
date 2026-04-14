class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lst={}
        res=[]
        l,r=0,0
        for i,j in enumerate(s):
            lst[j]=i
        for i,j in enumerate(s):
            l+=1
            r=max(r,lst[j])
            if i==r:
                res.append(l)
                l=0
        return res
