1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        max_sum = root.val
10        q = deque([root])
11        res = 1
12        curr_level = 1
13        while q:
14            level_sum = 0
15            for _ in range(len(q)):
16                visited = q.popleft()
17                level_sum += visited.val
18
19                if visited.left:
20                    q.append(visited.left)
21                if visited.right:
22                    q.append(visited.right)
23            
24            if level_sum > max_sum:
25                max_sum = level_sum
26                res = curr_level
27            
28            curr_level += 1
29        
30        return res
31