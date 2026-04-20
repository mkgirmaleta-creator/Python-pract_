class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        f = [""] * len(s)

        for i in range(len(indices)):
            f[indices[i]] = s[i]

        return "".join(f)