class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        largest_empty = len(nums) - 1
        res = [0] * len(nums)
        while l <= r:
            if nums[l]**2 <= nums[r]**2:
                res[largest_empty] = nums[r]**2
                r -= 1
            else:
                res[largest_empty] = nums[l]**2
                l += 1
            largest_empty -= 1
        return res