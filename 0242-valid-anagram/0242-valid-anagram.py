class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c={}
        d={}
        for i in s:
            if i in c:
                c[i]+=1
            else:c[i]=1
        for j in t:
            if j in d:
                d[j]+=1
            else:d[j]=1
        return d==c
        
        