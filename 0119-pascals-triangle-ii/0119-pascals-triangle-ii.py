class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[1]
        for i in range(rowIndex):
            p=[1]
            for j in range(len(a)-1):
                p.append(a[j]+a[j+1])
            p.append(1)
            a=p
        return a