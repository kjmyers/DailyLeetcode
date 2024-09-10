# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b != 0:
                a, b = b, a%b
            return a
        
        if not head.next:
            return head
        
        n1, n2 = head, head.next

        while n2:
            gcd_node = ListNode( gcd(n1.val, n2.val) )
            n1.next = gcd_node
            gcd_node.next = n2

            n1 = n2
            n2 = n2.next
        
        return head
