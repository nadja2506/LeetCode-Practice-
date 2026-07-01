"""
LeetCode 1 - Two Sum

Difficulty: Easy
Pattern: Arrays & Hash Map

Brute Force:
Time Complexity: O(n²)
Space Complexity: O(1)

Optimal:
Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
As we iterate through the array, store each number and its index in a hash map.
For every element, calculate the complement (target - current number). If the
complement already exists in the hash map, we have found the answer. Otherwise,
store the current number and continue.

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, value in enumerate(nums):
            answer = target - value
            if answer in hashMap: # check if we have already seen the complement
                return [index, hashMap[answer]]
            hashMap[value] = index

