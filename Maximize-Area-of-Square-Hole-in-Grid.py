1class Solution:
2    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
3        max_h = 0
4        max_v = 0
5        hBars.sort()
6        vBars.sort()
7
8        h_gap = 2
9        for i in range(len(hBars) - 1): 
10            if hBars[i+1] - hBars[i] == 1:
11                h_gap += 1
12            else:
13                max_h = max(max_h, h_gap)
14                h_gap = 2
15        max_h = max(max_h, h_gap)
16
17        v_gap = 2
18        for i in range(len(vBars) - 1):
19            if vBars[i+1] - vBars[i] == 1:
20                v_gap += 1
21            else:
22                max_v = max(max_v, v_gap)
23                v_gap = 2
24        max_v = max(max_v, v_gap)
25
26        if max_v >= max_h:
27            return max_h ** 2
28        else:
29            return max_v ** 2