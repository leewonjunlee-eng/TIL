from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            cur_next = current.next
            current.next = prev
            prev = current
            current = cur_next

        return prev


if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def values(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    head = ListNode(1, ListNode(2, ListNode(3)))
    assert values(Solution().reverseList(head)) == [3, 2, 1]
    assert Solution().reverseList(None) is None
