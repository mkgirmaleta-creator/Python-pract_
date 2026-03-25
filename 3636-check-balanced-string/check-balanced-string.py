class Solution:
    def isBalanced(self, num: str) -> bool:
        l1=list(map(int,num))
        n=len(l1)
        s1=0
        s2=0
        for i in range(0,n,2):
            s1+=l1[i]
        for i in range(1,n,2):
            s2+=l1[i]
        if s1==s2:
            return True
        else:
            return False


        