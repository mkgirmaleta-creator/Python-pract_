class Solution:
    def removeDuplicates(self, s: str) -> str:
       c=[s[0]]
       for i in range(1,len(s)):
        if len(c)!=0 and c[-1]==s[i]:c.pop()
        else:
            c.append(s[i])
       return "".join(c)
