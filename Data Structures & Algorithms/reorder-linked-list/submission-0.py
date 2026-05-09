from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        q = deque()

        curr = head
        while curr:
            q.append(curr)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy

        toggle = True

        while q:
            if toggle:
                curr.next = q.popleft()
            else:
                curr.next = q.pop()

            curr = curr.next
            toggle = not toggle

        curr.next = None