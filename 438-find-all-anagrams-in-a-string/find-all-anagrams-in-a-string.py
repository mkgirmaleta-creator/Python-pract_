class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        phash,shash={},{}
        for i in range(len(p)):
            phash[p[i]]=phash.get(p[i],0)+1
            shash[s[i]]=shash.get(s[i],0)+1
        c=[0] if phash==shash else []
        l=0
        for r in range(len(p),len(s)):
            shash[s[r]]=shash.get(s[r],0)+1
            shash[s[l]]-=1
            if shash[s[l]]==0:
                shash.pop(s[l])
            l+=1
            if shash==phash:
                c.append(l)
        return c

       