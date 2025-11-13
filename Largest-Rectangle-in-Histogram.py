class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            currheight = heights[i]
            while stack and currheight < heights[stack[-1]]:
                    topindex = stack.pop()
                    topheight = heights[topindex]
                    width = i if not stack else i - stack[-1] - 1
                    area = topheight * width
                    res = max(res, area)
            stack.append(i)
    
        return res
