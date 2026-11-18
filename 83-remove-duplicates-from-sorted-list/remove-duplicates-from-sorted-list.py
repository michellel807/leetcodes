# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        numbers = set()

        while head:
            numbers.add(head.val)
            head = head.next
        sorted_nums = sorted(numbers)

        output = ListNode()
        current = output
        for i in sorted_nums:
            current.next = ListNode(i)
            current = current.next


        return output.next