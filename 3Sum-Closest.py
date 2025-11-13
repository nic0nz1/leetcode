class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minaway = inf
        res = 0
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currsum = nums[i] + nums[l] + nums[r]
                away = nums[i] + nums[l] + nums[r] - target
                if abs(away) < minaway:
                    minaway = abs(away)
                    res = currsum
                if away == 0:
                    return res
                elif away < 0:
                    l += 1
                else:
                    r -= 1
        return res