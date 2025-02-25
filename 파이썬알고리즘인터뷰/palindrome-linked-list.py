# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums: Deque = collections.deque()

        if not head:
            return True
        
        node = head
        while node != None:
            nums.append(node.val)
            node = node.next
        
        # while len(nums) > 1:
        #     if nums.pop() != nums.popleft():
        #         return False
        reversed_nums = nums.reverse()
        if reversed_nums == nums:
            return True
        else:
            return False