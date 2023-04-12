# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            ret = list1
            list1 = list1.next
        else:
            ret = list2
            list2 = list2.next
            
        head = ret
        
        while list1 and list2:
            
            if list1.val < list2.val:
                ret.next = list1
                ret = ret.next
                list1 = list1.next
            else:
                ret.next = list2
                ret = ret.next
                list2 = list2.next
        
        if list1:
            ret.next = list1
        elif list2:
            ret.next = list2
        
        return head
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        list1 = lists[0]
        for i in range(1,len(lists)):
            list2 = lists[i]
            list1 = self.mergeTwoLists(list1,list2)
        
        return list1

