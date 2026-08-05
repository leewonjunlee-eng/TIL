from __future__ import annotations
from typing import Optional

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)
        copies = {None: None}
        current = dummy
        original = head

        while original:
            current.next = Node(original.val)
            current = current.next
            copies[original] = current
            original = original.next

        original = head
        current = dummy.next
        while original:
            current.random = copies[original.random]
            current = current.next
            original = original.next

        return dummy.next


if __name__ == "__main__":
    class Node:
        def __init__(self, x: int, next=None, random=None):
            self.val = x
            self.next = next
            self.random = random

    first = Node(7)
    second = Node(13)
    third = Node(11)
    first.next, second.next = second, third
    second.random, third.random = first, first

    copied = Solution().copyRandomList(first)
    assert copied is not first
    assert copied.val == 7
    assert copied.next.val == 13
    assert copied.next.next.val == 11
    assert copied.next.random is copied
    assert copied.next.next.random is copied
