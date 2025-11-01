# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0,next=head)

        delete = set(nums)

        prev = dummy
        cur = head
        while cur:
            if cur.val in delete:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next

        return dummy.next
