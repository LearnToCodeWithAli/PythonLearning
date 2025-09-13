# Leeetcode #1
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that
# they add up to target.
#
# You may assume that each input would have exactly one
# solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import Optional


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
#
# nums = [2,7,11,15]
# target = 9
#
# temp = {}
#
# index = 0
# for each in nums:
#     if(each in temp.values()):
#         return [ temp[], index]
#
#
# print(temp)


# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit.
#
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any
# leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = l1

        text_1 = self.get_num_as_reverse_string(l1)

        text_2 = self.get_num_as_reverse_string(l2)

        int_1 = int(text_1)
        int_2 = int(text_2)

        sum = str(int_1 + int_2)[::-1]

        l1 = head
        for digit in sum:
            l1.val = digit
            l1 = l1.next

        return head

    def get_num_as_reverse_string(self, node):
        text = ""

        while (node):
            text += str(node.val)
            node = node.next

        return text[::-1]


#Ali, have you used type checking with py yet ?

temp2 = ListNode(val=3)
temp1 = ListNode(val=4, next=temp2)
l1 = ListNode(val=2, next=temp1)

temp4 = ListNode(val=4)
temp3 = ListNode(val=6,next=temp4)
l2 = ListNode(val=5,next=temp3)

solution = Solution()
print(solution.add_two_numbers(l1,l2))

# l1 = [2,4,3], l2 = [5,6,4]
























