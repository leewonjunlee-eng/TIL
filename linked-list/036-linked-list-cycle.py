from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    solution = Solution()
    assert solution.hasCycle(None) is False

    first = ListNode(1)
    first.next = ListNode(2)
    assert solution.hasCycle(first) is False

    first.next.next = ListNode(3)
    first.next.next.next = first.next
    assert solution.hasCycle(first) is True
