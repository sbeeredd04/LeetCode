"""
This module automatically generates test cases for LeetCode problems
based on common input patterns and edge cases.

It can be used to quickly generate test cases for new problems
or to generate additional edge cases for existing problems.
"""

from typing import List, Dict, Any, Callable, Tuple
import random
import string

def generate_test_cases(problem_type: str, num_cases: int = 5, custom_params: Dict = None) -> List[Tuple]:
    """
    Generate test cases for common LeetCode problem types.
    
    Args:
        problem_type: The type of problem (array, string, tree, etc.)
        num_cases: Number of test cases to generate
        custom_params: Custom parameters for test case generation
        
    Returns:
        List of (args, expected_output) tuples for testing
    """
    generators = {
        "array": generate_array_test_cases,
        "string": generate_string_test_cases,
        "anagram": generate_anagram_test_cases,
        "bst": generate_binary_search_tree_test_cases,
        "linked_list": generate_linked_list_test_cases,
        "two_sum": generate_two_sum_test_cases,
    }
    
    if problem_type not in generators:
        raise ValueError(f"Unknown problem type: {problem_type}. Available types: {list(generators.keys())}")
    
    params = custom_params or {}
    return generators[problem_type](num_cases, **params)

def generate_array_test_cases(num_cases: int, min_size: int = 1, max_size: int = 10,
                             min_value: int = -100, max_value: int = 100, 
                             include_empty: bool = True, **kwargs) -> List[Tuple]:
    """Generate test cases with array inputs."""
    test_cases = []
    
    # Empty array case if requested
    if include_empty:
        test_cases.append((([],), []))
    
    # Generate random arrays
    for _ in range(num_cases):
        size = random.randint(min_size, max_size)
        array = [random.randint(min_value, max_value) for _ in range(size)]
        
        # Placeholder for expected output - you'll need to compute this
        # based on your specific algorithm
        expected_output = sorted(array)  # Example: sorting
        
        test_cases.append(((array,), expected_output))
    
    return test_cases

def generate_string_test_cases(num_cases: int, min_length: int = 1, max_length: int = 10,
                              charset: str = string.ascii_lowercase, 
                              include_empty: bool = True, **kwargs) -> List[Tuple]:
    """Generate test cases with string inputs."""
    test_cases = []
    
    # Empty string case if requested
    if include_empty:
        test_cases.append((("",), ""))
    
    # Generate random strings
    for _ in range(num_cases):
        length = random.randint(min_length, max_length)
        s = ''.join(random.choice(charset) for _ in range(length))
        
        # Placeholder for expected output - you'll need to compute this
        # based on your specific algorithm
        expected_output = s  # Example: identity function
        
        test_cases.append(((s,), expected_output))
    
    return test_cases

def generate_anagram_test_cases(num_cases: int, min_length: int = 1, max_length: int = 10,
                               include_edge_cases: bool = True, **kwargs) -> List[Tuple]:
    """Generate test cases specifically for anagram problems."""
    test_cases = []
    
    # Add some edge cases
    if include_edge_cases:
        # Same strings
        test_cases.append((("a", "a"), True))
        test_cases.append((("", ""), True))
        
        # Different lengths
        test_cases.append((("a", ""), False))
        test_cases.append((("a", "ab"), False))
        
        # Same letters, different counts
        test_cases.append((("aab", "abb"), False))
        
        # Completely different
        test_cases.append((("abc", "xyz"), False))
    
    # Generate random anagram pairs
    for _ in range(num_cases):
        length = random.randint(min_length, max_length)
        chars = [random.choice(string.ascii_lowercase) for _ in range(length)]
        s = ''.join(chars)
        
        # Create anagram by shuffling
        t_chars = chars.copy()
        random.shuffle(t_chars)
        t = ''.join(t_chars)
        
        test_cases.append(((s, t), True))
        
        # Also add some non-anagrams
        if length > 0:
            # Replace one character to make it non-anagram
            pos = random.randint(0, length-1)
            old_char = t_chars[pos]
            while True:
                new_char = random.choice(string.ascii_lowercase)
                if new_char != old_char:
                    break
                    
            t_chars[pos] = new_char
            t_non_anagram = ''.join(t_chars)
            test_cases.append(((s, t_non_anagram), False))
    
    return test_cases

def generate_binary_search_tree_test_cases(num_cases: int, **kwargs):
    """Placeholder for BST test case generation."""
    # This would need a TreeNode class definition and specialized handling
    return [(([1, 2, 3, 4, 5],), None)] * num_cases

def generate_linked_list_test_cases(num_cases: int, **kwargs):
    """Placeholder for linked list test case generation."""
    # This would need a ListNode class definition and specialized handling
    return [(([1, 2, 3, 4, 5],), None)] * num_cases

def generate_two_sum_test_cases(num_cases: int, min_size: int = 2, max_size: int = 10,
                               min_value: int = -100, max_value: int = 100, **kwargs) -> List[Tuple]:
    """Generate test cases specifically for the Two Sum problem."""
    test_cases = []
    
    for _ in range(num_cases):
        size = random.randint(min_size, max_size)
        nums = [random.randint(min_value, max_value) for _ in range(size)]
        
        # Ensure there is a valid solution
        i = random.randint(0, size-2)
        j = random.randint(i+1, size-1)
        target = nums[i] + nums[j]
        
        # The expected answer is the indices
        expected_output = [i, j]
        
        test_cases.append(((nums, target), expected_output))
    
    return test_cases

# Export for easy importing
__all__ = ['generate_test_cases']
