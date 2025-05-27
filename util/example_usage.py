"""
Example showing how to use the LeetCode tester utility.
This demonstrates various ways to test your solution.
"""

from util.leetcode_tester import LeetCodeTester, run_tests
from typing import List

# Import your solution class
# For this example, we'll use the validAnagramAlt.py solution
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '242'))
from validAnagramAlt import Solution

def test_with_tester_class():
    """Shows how to test using the LeetCodeTester class with manual test case addition."""
    print("\n\nMethod 1: Using the LeetCodeTester class")
    
    # Create a tester instance
    tester = LeetCodeTester(Solution, "isAnagram")
    
    # Add test cases
    tester.add_test("anagram", "nagaram", expected_output=True, test_name="Valid Anagram")
    tester.add_test("rat", "car", expected_output=False, test_name="Invalid Anagram")
    tester.add_test("a", "ab", expected_output=False, test_name="Different Length")
    tester.add_test("aa", "aa", expected_output=True, test_name="Identical Strings")
    tester.add_test("aab", "baa", expected_output=True, test_name="Same Characters")
    tester.add_test("aacc", "ccac", expected_output=False, test_name="Different Count")
    
    # Run all tests
    tester.run_all_tests()

def test_with_run_tests_function():
    """Shows how to test using the simpler run_tests function."""
    print("\n\nMethod 2: Using the run_tests helper function")
    
    # Define test cases as (args, expected_output) tuples
    test_cases = [
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
        (("a", "ab"), False),
        (("aa", "aa"), True), 
        (("aab", "baa"), True),
        (("aacc", "ccac"), False),
    ]
    
    # Run tests
    run_tests(Solution, "isAnagram", test_cases)

def test_with_autodetect():
    """Shows how method name can be auto-detected for simple classes."""
    print("\n\nMethod 3: Using auto-detection of method name")
    
    # Create a simplified test class with just one method
    class SimpleAnagramSolution:
        def isAnagram(self, s: str, t: str) -> bool:
            return sorted(s) == sorted(t)
    
    # Define test cases
    test_cases = [
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
    ]
    
    # Run tests - method_name will be auto-detected
    run_tests(SimpleAnagramSolution, test_cases=test_cases)

if __name__ == "__main__":
    # Run the examples
    test_with_tester_class()
    test_with_run_tests_function()
    test_with_autodetect()
    
    # You can also do one-off tests for quick debugging
    print("\n\nQuick Test:")
    run_tests(Solution, "isAnagram", [
        (("hello", "olleh"), True),
        (("hello", "world"), False),
    ])
