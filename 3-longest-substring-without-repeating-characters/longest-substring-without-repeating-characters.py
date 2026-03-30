class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        st=[]
        t=0
        while r<len(s):
            if s[r] not in st:
                st.append(s[r])
                t=max(t,len(st))
                r+=1
            else:
                st=[]
                l+=1
                r=l
        return t

        