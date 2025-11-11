class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            curr = min(height[l], height[r]) * (r-l)
            if curr > res:
                res = curr
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return res