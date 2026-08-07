from __future__ import annotations

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        heap = []
        for i in range(len(lists)):
            head = lists[i]
            if head is not None:
                heapq.heappush(heap, (head.val, i, head))

        while heap:
            value, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


def build(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def values(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    solution = Solution()
    assert values(
        solution.mergeKLists(
            [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
        )
    ) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert solution.mergeKLists([]) is None
    assert solution.mergeKLists([None, None]) is None
    assert values(solution.mergeKLists([build([]), build([1]), build([1])])) == [1, 1]
