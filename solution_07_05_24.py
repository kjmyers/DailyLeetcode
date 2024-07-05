# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        count = 1
        crits = []
        left = head
        head = head.next
        while head.next:
            if (left.val > head.val and head.next.val > head.val or
                left.val < head.val and head.next.val < head.val):
                crits.append(count)
            count += 1
            left = head
            head = head.next

        if len(crits) < 2:
            return [-1,-1]

        ret = [crits[1] - crits[0],0]
        ret[1] = crits[-1] - crits[0]
        for i in range(2, len(crits)):
            ret[0] = min(ret[0], crits[i] - crits[i-1])

        return ret
