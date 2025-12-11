1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        distincts = set()
4        for num in nums:
5            if num not in distincts:
6                distincts.add(num)
7            else:
8                return True
9        return False