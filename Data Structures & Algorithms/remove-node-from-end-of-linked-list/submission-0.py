
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = head
        slow = dummy  # slow starts at dummy
        
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # slow.next is the node to remove
        to_remove = slow.next
        slow.next = to_remove.next
        # to_remove.next = None  # optional cleanup
        
        return dummy.next