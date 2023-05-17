# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next
        
        ret = 0
        n = len(arr)
        for i in range(n//2):
            ret = max(ret, arr[i] + arr[n-1-i])
        
        return ret
