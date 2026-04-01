class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        l,r=0,n-1
        c=0
        while l<r:
            if people[l]+people[r]<=limit:
                c+=1
                l+=1
                r-=1
            elif people[l]>=limit:
                c+=1
                l+=1
            elif people[r]>=limit:
                c+=1
                r-=1
            elif people[l]+people[r]>=limit:
                 c+=1
                 r-=1
        if r==l:
            c+=1

        return c







