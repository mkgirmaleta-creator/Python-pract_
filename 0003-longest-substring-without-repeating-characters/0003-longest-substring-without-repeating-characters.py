class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k=[]
        m=0
        l=set(s)
        if len(s)==len(l):return len(s)
        for i in range(len(s)):
            if s[i] not in k :
                k.append(s[i])
                
            else:
                idx = k.index(s[i])
                k = k[idx + 1:]
                k.append(s[i])
            m=max(m,len(k))
        return m



        