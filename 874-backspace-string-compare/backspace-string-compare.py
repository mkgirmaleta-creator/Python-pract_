class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss=[]
      
        for i in s:
            if i!='#':
                ss.append(i)
            else:
                if ss:
                    ss.pop()
        s=[]
        for i in t :
             if i!='#':
                s.append(i)
             else:
                if s:
                    s.pop()
        return ss==s
        