# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        mid = head
        s = []

        l = 0
        while fast:
            l += 1
            fast = fast.next
        fast = head

        while fast and fast.next:
            s.append(mid.val)
            fast = fast.next.next
            mid = mid.next

        if l % 2:
            mid = mid.next

        while mid:
            if mid.val != s.pop():
                return False
            mid = mid.next      

        return True
