# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p1 = list1
        for _ in range(a-1):
            p1 = p1.next
        p2 = p1
        for _ in range(b-a+2):
            p2 = p2.next
        
        p1.next = list2
        while p1.next:
            p1 = p1.next
        p1.next = p2

        return list1

