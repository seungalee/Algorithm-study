# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        output = dummy

        while l1 and l2:
            output.val += (l1.val + l2.val)
            over_ten = False
            if output.val >= 10:
                output.val -= 10
                over_ten = True
            if over_ten:
                output.next = ListNode(1)
            elif l1.next or l2.next:  # l1 또는 l2에 남은 노드가 있을 때만 새 노드 추가
                output.next = ListNode(0)
            output = output.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            output.val += l1.val
            if output.val >= 10:
                output.val -= 10
                output.next = ListNode(1)
            elif l1.next:  # l1에 남은 노드가 있을 때만 새 노드 추가
                output.next = ListNode(0)
            output = output.next
            l1 = l1.next

        while l2:
            output.val += l2.val
            if output.val >= 10:
                output.val -= 10
                output.next = ListNode(1)
            elif l2.next:  # l2에 남은 노드가 있을 때만 새 노드 추가
                output.next = ListNode(0)
            output = output.next
            l2 = l2.next
        
        return dummy
