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

        if list1.val <= list2.val:
            head = list1
            cur = list1.next
            second = list2
        else:
            head = list2
            cur = list2.next
            second = list1

        joined = head

        while cur and second:
            if cur.val <= second.val:
                joined.next = cur
                cur = cur.next
            else:
                joined.next = second
                second = second.next

            joined = joined.next

        if cur:
            joined.next = cur
        else:
            joined.next = second

        return head


        
        