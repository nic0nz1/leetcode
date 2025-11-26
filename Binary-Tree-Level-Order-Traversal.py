1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if root == None:
10            return []
11        res = []
12        q = deque()
13        q.append(root)
14        while q:
15            minires = []
16            for i in range(len(q)):
17                curr = q.popleft()
18                minires.append(curr.val)
19                if curr.left:
20                    q.append(curr.left)
21                if curr.right:
22                    q.append(curr.right) 
23            res.append(minires)
24        return res
25
26                
27                
28
29