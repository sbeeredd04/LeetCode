"""
LeetCode Test Utility

This module provides tools for testing LeetCode solutions with
formatted output and result verification.
"""

import time
import traceback
from typing import Any, Callable, Dict, List, Tuple, Union
import sys
import inspect
from termcolor import colored
from tabulate import tabulate

# Try importing color support - fall back to simple formatting if not available
try:
    from termcolor import colored
    HAS_COLORS = True
except ImportError:
    HAS_COLORS = False
    def colored(text, color=None, *args, **kwargs):
        return text

# Try importing tabulate for tables - fall back to simple formatting if not available
try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False
    def tabulate(data, headers=None, tablefmt=None):
        result = []
        if headers:
            result.append("  ".join(str(h) for h in headers))
            result.append("-" * 40)
        for row in data:
            result.append("  ".join(str(cell) for cell in row))
        return "\n".join(result)

def format_value(value: Any) -> str:
    """Format a value for display in test results."""
    if isinstance(value, list):
        return str(value)
    elif isinstance(value, str):
        return f'"{value}"'
    else:
        return str(value)

class LeetCodeTester:
    def __init__(self, solution_class, method_name: str = None):
        """
        Initialize the tester with a solution class.
        
        Args:
            solution_class: The solution class containing the method to test
            method_name: The method name to test (optional - will detect if not provided)
        """
        self.solution_class = solution_class
        self._method_name = method_name
        self.tests = []
        self.test_results = []
        self.execution_times = []
        
        # Auto-detect method if not provided
        if not method_name:
            methods = [name for name, func in inspect.getmembers(solution_class, predicate=inspect.isfunction)
                      if not name.startswith('_')]
            if len(methods) == 1:
                self._method_name = methods[0]
            else:
                print(f"Multiple methods found in solution class: {methods}")
                print("Please specify which one to test using method_name parameter")
    
    @property
    def method_name(self):
        """Get the method name being tested."""
        return self._method_name
    
    def add_test(self, *args, expected_output=None, test_name=None):
        """
        Add a test case.
        
        Args:
            *args: The arguments to pass to the solution method
            expected_output: The expected output for verification
            test_name: Optional name for the test case
        """
        if test_name is None:
            test_name = f"Test {len(self.tests) + 1}"
            
        self.tests.append({
            "name": test_name,
            "args": args,
            "expected": expected_output
        })
        return self
    
    def _run_single_test(self, test):
        """Run a single test and collect results."""
        instance = self.solution_class()
        method = getattr(instance, self.method_name)
        
        start_time = time.time()
        try:
            actual_output = method(*test["args"])
            execution_time = time.time() - start_time
            
            is_correct = actual_output == test["expected"]
            
            result = {
                "name": test["name"],
                "args": test["args"],
                "expected": test["expected"],
                "actual": actual_output,
                "passed": is_correct,
                "time": execution_time,
                "error": None
            }
        except Exception as e:
            execution_time = time.time() - start_time
            result = {
                "name": test["name"],
                "args": test["args"],
                "expected": test["expected"],
                "actual": None,
                "passed": False,
                "time": execution_time,
                "error": str(e),
                "traceback": traceback.format_exc()
            }
        
        return result
    
    def run_all_tests(self, verbose=True):
        """Run all test cases and print results."""
        if not self.method_name:
            print("Error: No method specified for testing")
            return
        
        print(f"\n{'='*60}")
        print(f"Running tests for: {self.solution_class.__name__}.{self.method_name}")
        print(f"{'='*60}")
        
        self.test_results = []
        self.execution_times = []
        
        for i, test in enumerate(self.tests):
            result = self._run_single_test(test)
            self.test_results.append(result)
            self.execution_times.append(result["time"])
            
            if verbose:
                self._print_test_result(result, i+1, len(self.tests), verbose)
        
        self._print_summary()
        return self.test_results
    
    def _print_test_result(self, result, test_num, total_tests, verbose=False):
        """Print the result of a single test."""
        if result["passed"]:
            status = colored("✓ PASS", "green") if HAS_COLORS else "✓ PASS"
        else:
            status = colored("✗ FAIL", "red") if HAS_COLORS else "✗ FAIL"
            
        print(f"\nTest {test_num}/{total_tests}: {result['name']} - {status}")
        print(f"  {'_'*50}")
        
        # Print test inputs
        if len(result["args"]) == 1:
            print(f"  Input: {format_value(result['args'][0])}")
        else:
            for i, arg in enumerate(result["args"]):
                print(f"  Input #{i+1}: {format_value(arg)}")
        
        # Print expected vs actual
        print(f"  Expected: {format_value(result['expected'])}")
        print(f"  Actual:   {format_value(result['actual'])}")
        print(f"  Time:     {result['time']*1000:.2f} ms")
        
        # Print error if any
        if result["error"]:
            print(colored(f"\n  ERROR: {result['error']}", "red") if HAS_COLORS else f"\n  ERROR: {result['error']}")
            if verbose:
                print(result["traceback"])
    
    def _print_summary(self):
        """Print a summary of all test results."""
        passed = sum(1 for r in self.test_results if r["passed"])
        total = len(self.test_results)
        
        print("\n" + "="*60)
        if passed == total:
            status = colored(f"All {passed}/{total} tests PASSED!", "green") if HAS_COLORS else f"All {passed}/{total} tests PASSED!"
        else:
            status = colored(f"{passed}/{total} tests passed.", "yellow") if HAS_COLORS else f"{passed}/{total} tests passed."
        
        print(f"Summary: {status}")
        print(f"Average time: {sum(self.execution_times)*1000/total:.2f} ms")
        print("="*60)
        
        # Show table summary
        if HAS_TABULATE and len(self.test_results) > 0:
            table_data = []
            for i, result in enumerate(self.test_results):
                status = "✓" if result["passed"] else "✗"
                args_str = ", ".join(format_value(arg) for arg in result["args"])
                table_data.append([
                    i+1,
                    result["name"],
                    status,
                    args_str[:30] + ("..." if len(args_str) > 30 else ""),
                    format_value(result["expected"])[:30] + ("..." if len(format_value(result["expected"])) > 30 else ""),
                    f"{result['time']*1000:.1f} ms"
                ])
            
            print("\nResults Table:")
            print(tabulate(table_data, headers=["#", "Test Name", "Status", "Inputs", "Expected", "Time"], 
                           tablefmt="pretty"))
            print()

def run_tests(solution_class, method_name=None, test_cases=None):
    """
    Quick function to run tests on a solution class.
    
    Args:
        solution_class: The solution class to test
        method_name: The method to test (auto-detected if None)
        test_cases: List of (args, expected) tuples where args is a tuple of arguments
    
    Example:
        run_tests(Solution, "twoSum", [
            ((nums, target), expected_result),
            ((nums2, target2), expected_result2),
        ])
    """
    tester = LeetCodeTester(solution_class, method_name)
    
    if not test_cases:
        print("No test cases provided!")
        return
    
    for i, (args, expected) in enumerate(test_cases):
        if not isinstance(args, tuple):
            args = (args,)
        tester.add_test(*args, expected_output=expected)
    
    tester.run_all_tests()

# Export for easy importing
__all__ = ['LeetCodeTester', 'run_tests']
