# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        n = -1
        curr = head
        values = []
        res = 0
        while curr:
            values.append(curr.val)
            n += 1
            curr = curr.next
        for num in values:
            res += num * (2**n)
            n -=1
        return res