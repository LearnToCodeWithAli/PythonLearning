# # Leetcode Easy #1 - Two Sum
#
# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# # You can return the answer in any order.
#
#
# # Input: nums = [2,7,11,15], target = 9
#
# def solution(nums, target):
#
#     for x in range(len(nums)):
#         for y in range(len(nums)):
#             if x != y and nums[x] + nums[y] == target:
#                 return [x,y]
#
# def solution2(nums, target):
#     dictionary = dict()
#
#     for x in range(len(nums)):
#         dictionary[nums[x]] = x
#         solution = target - nums[x]
#
#         if solution in dictionary.keys():
#             return [x,dictionary[solution]]
#
#
#
# print(solution([2,7,11,15],9))
# print(solution([3,2,4],6))
# print(solution([3,3], 6))
#
# print(solution2([2,7,11,15],9))
# print(solution2([3,2,4],6))
# print(solution2([3,3], 6))





























