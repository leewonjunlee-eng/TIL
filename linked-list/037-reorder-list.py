from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow.next
        slow.next = None

        while current:
            cur_next = current.next
            current.next = prev
            prev = current
            current = cur_next

        cur1 = head
        cur2 = prev
        while cur2:
            next1 = cur1.next
            next2 = cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1 = next1
            cur2 = next2


if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def build(values):
        head = None
        for value in reversed(values):
            head = ListNode(value, head)
        return head

    def values(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    solution = Solution()
    single = build([1])
    solution.reorderList(single)
    assert values(single) == [1]

    even = build([1, 2, 3, 4])
    solution.reorderList(even)
    assert values(even) == [1, 4, 2, 3]

    odd = build([1, 2, 3, 4, 5])
    solution.reorderList(odd)
    assert values(odd) == [1, 5, 2, 4, 3]
