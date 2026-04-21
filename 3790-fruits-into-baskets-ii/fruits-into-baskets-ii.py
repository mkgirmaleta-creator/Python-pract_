class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        for fruit in fruits:
            u=1
            for i in range(len(baskets)):
                if fruit<=baskets[i]:
                    baskets[i]=0
                    u=0
                    break
            c+=u
        return c

       