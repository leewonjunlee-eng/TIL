from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def getKthNode(
        self, group_previous: ListNode, k: int
    ) -> Optional[ListNode]:
        kth = group_previous

        for _ in range(k):
            kth = kth.next
            if kth is None:
                return None

        return kth

    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        group_previous: ListNode = dummy

        while True:
            kth = self.getKthNode(group_previous, k)
            if kth is None:
                break

            next_group = kth.next
            group_head = group_previous.next
            assert group_head is not None
            kth.next = None

            reversed_head = self.reverseList(group_head)
            group_previous.next = reversed_head

            # 뒤집히기 전의 첫 노드가 뒤집힌 그룹의 마지막 노드가 된다.
            group_head.next = next_group
            group_previous = group_head

        return dummy.next


def build(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_values(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    solution = Solution()
    assert to_values(solution.reverseKGroup(build([1, 2, 3, 4, 5]), 2)) == [
        2,
        1,
        4,
        3,
        5,
    ]
    assert to_values(solution.reverseKGroup(build([1, 2, 3, 4, 5]), 3)) == [
        3,
        2,
        1,
        4,
        5,
    ]
    assert to_values(solution.reverseKGroup(build([1, 2]), 3)) == [1, 2]
    assert to_values(solution.reverseKGroup(build([1, 2, 3]), 1)) == [1, 2, 3]
    assert solution.reverseKGroup(None, 2) is None
