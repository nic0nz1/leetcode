1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        def dfs(node):
10            if not node:
11                return (None, 0)
12            left_node, left_depth = dfs(node.left)
13            right_node, right_depth = dfs(node.right)
14
15            if left_depth > right_depth:
16                return (left_node, left_depth + 1)
17            elif left_depth < right_depth:
18                return (right_node, right_depth + 1)
19            else:
20                return (node, left_depth + 1)
21        node, depth = dfs(root)
22        return node
23            
24
25