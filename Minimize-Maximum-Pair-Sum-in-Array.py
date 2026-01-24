1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        return nums.sort() or max(nums[i] + nums[len(nums)-i-1] for i in range(len(nums) // 2))