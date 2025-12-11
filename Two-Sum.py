1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3      memo = {}
4      for i,v in enumerate(nums):
5        remaining = target - v
6        if remaining in memo:
7          return [i, memo[remaining]]
8        memo[v] = i
9        