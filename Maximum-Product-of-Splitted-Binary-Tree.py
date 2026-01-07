1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        res = 0
10        
11        def get_total_sum(node):
12            if not node:
13                return 0
14            return node.val + get_total_sum(node.left) + get_total_sum(node.right)
15        
16        total_sum = get_total_sum(root)
17
18        subtree_sums = []
19
20        def dfs(node):
21            if not node:
22                return 0
23            
24            left_sum = dfs(node.left)
25            right_sum = dfs(node.right)
26
27            current_sum = node.val + left_sum + right_sum
28
29            subtree_sums.append(current_sum)
30
31            return current_sum
32
33        dfs(root)
34
35        for subtree_sum in subtree_sums:
36            res = max(res, (total_sum - subtree_sum) * subtree_sum)
37        return res % (10**9 + 7)