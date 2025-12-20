1class Solution:
2    def minDeletionSize(self, strs: List[str]) -> int:
3        res = 0
4        for i in range(len(strs[0])):
5            for j in range(1,len(strs)):
6                if strs[j][i] < strs[j-1][i]:
7                    res += 1
8                    break
9        return res
10
11