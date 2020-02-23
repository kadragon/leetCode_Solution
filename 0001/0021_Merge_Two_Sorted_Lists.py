"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, *args, **kwargs):
        if type(args[0]) is int:
            self.val = args[0]
            self.next = None

        if type(args[0]) is list:
            self.val = args[0][0] if len(args[0]) > 0 else None
            self.next = ListNode(args[0][1:]) if len(args[0]) > 1 else None

    def print_list_val(self):
        target = self

        while target.next is not None:
            print(target.val, end=' > ')
            target = target.next

        print(target.val)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        next_node = l3
        while l1 is not None or l2 is not None:
            if l1 is None:
                next_node.next = l2
                break
            if l2 is None:
                next_node.next = l1
                break

            if l1.val <= l2.val:
                next_node.next = l1
                next_node = next_node.next
                l1 = l1.next
            elif l1.val > l2.val:
                next_node.next = l2
                next_node = next_node.next
                l2 = l2.next

        return l3.next


"""
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

s = Solution()

l1 = ListNode([1, 2, 4])
l2 = ListNode([1, 3, 4])

answer = s.mergeTwoLists(l1, l2)
answer.print_list_val()


"""
Runtime: 32 ms, faster than 85.44% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""
