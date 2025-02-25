# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        odd_nums = dummy
        even_nums = ListNode(0)
        pointer = even_nums

        while head and head.next:
            odd_nums.next = ListNode(head.val)
            odd_nums = odd_nums.next
            head = head.next
            even_nums.next = ListNode(head.val)
            even_nums = even_nums.next
            head = head.next
        
        if head:
            odd_nums.next = ListNode(head.val)
            odd_nums = odd_nums.next
        
        odd_nums.next = pointer.next
        return dummy.next

