1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        res = 0
4        for i in range(len(points)-1):
5            x, y = points[i]
6            next_x, next_y = points[i+1]
7            res += max(abs(next_x - x), abs(next_y - y))
8        return res