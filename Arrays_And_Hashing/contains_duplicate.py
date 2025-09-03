"""
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
import unittest

from typing import List


"""
Intuition - A set is an unordered collection of distinct items. 
Hence, when we convert the input list to a set and check its length against the length of the input array, we can identify if we have seen duplicates
Run time complexity - O(n) 
Space Complexity - O(n)
Can we do better? Not really, so this is the best solution we can get to
"""

def contains_duplicate(nums: List) -> bool:
	return False if len(set(nums)) == len(nums) else True
	

class TestContainsDuplicate(unittest.TestCase):

	def test_empty_list(self):
		self.assertFalse(contains_duplicate([]))

	def test_single_element_input_list(self):
		self.assertFalse(contains_duplicate([1]))	

	def test_multi_element_input_list_with_duplicates(self):
		self.assertTrue(contains_duplicate([1,1]))

	def test_multi_element_input_list_without_duplicates(self):
		self.assertFalse(contains_duplicate([1,2]))

if __name__ == "__main__":
	unittest.main()