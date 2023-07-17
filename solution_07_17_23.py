# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            if node.next == None:
                return node
            
            newHead = reverse(node.next)

            node.next.next = node

            node.next = None

            return newHead
        
        l1 = reverse(l1)
        l2 = reverse(l2)

        print(l1)
        print(l2)

        prev = None
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = 0
            if val > 9:
                val -= 10
                carry += 1
            cur = ListNode(val, prev)
            l1 = l1.next
            l2 = l2.next
            prev = cur
        
        while l1:
            val = l1.val + carry
            carry = 0
            if val > 9:
                val -= 10
                carry += 1
            cur = ListNode(val, prev)
            l1 = l1.next
            prev = cur
        
        while l2:
            val = l2.val + carry
            carry = 0
            if val > 9:
                val -= 10
                carry += 1
            cur = ListNode(val, prev)
            l2 = l2.next
            prev = cur
        
        if carry:
            cur = ListNode(carry, prev)

        return cur
