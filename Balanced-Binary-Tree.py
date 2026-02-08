1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        self.balanced = True
10
11        def dfs(node):
12            if node is None:
13                return 0
14            
15            left = dfs(node.left)
16            right = dfs (node.right)
17
18            if abs(left-right) > 1:
19                self.balanced = False
20            
21            return max(left, right) + 1
22        
23        dfs(root)
24        return self.balanced