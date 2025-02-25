# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        dummy = ListNode(0)
        output = dummy

        while nums:
            output.next = ListNode(nums.pop())
            output = output.next
        return dummy.next
            
