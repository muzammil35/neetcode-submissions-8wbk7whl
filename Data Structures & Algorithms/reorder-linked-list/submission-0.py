# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = head
        i = 0
        while p1:
            cur = p1.next
            if i % 2 == 0:
                prev = cur
                while cur!= None and cur.next != None:
                    prev = cur
                    cur = cur.next
                if cur != None:
                    temp = p1.next
                    p1.next = cur
                    cur.next = temp
                    prev.next = None
            p1 = p1.next
            i += 1

                
        
                
                




        
        