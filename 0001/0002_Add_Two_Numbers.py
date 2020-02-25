# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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


def cal_list_value(node: ListNode) -> int:
    a = ''
    while True:
        a = str(node.val) + a
        if node.next is None:
            break
        node = node.next

    return int(a)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c = cal_list_value(l1) + cal_list_value(l2)
        answer = ListNode(0)
        p = answer

        for _ in range(len(str(c))):
            p.next = ListNode(c % 10)
            p = p.next
            c = c // 10

        return answer.next


s = Solution()
s.addTwoNumbers(ListNode([2, 4, 3]), ListNode([5, 6, 4])).print_list_val()

"""
Runtime: 76 ms, faster than 30.04% of Python3 online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

https://leetcode.com/problems/add-two-numbers/discuss/352181/Python3-Carry-sum10
"""