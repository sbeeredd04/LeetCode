# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

## Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples
```python
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = ""
Output: true
Explanation: An empty string reads the same forward and backward.
```

## Constraints
- `1 ≤ s.length ≤ 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## 🧠 Thought Process Evolution

### 🎯 **Problem Analysis**
1. **Preprocessing**: Convert to lowercase + remove non-alphanumeric
2. **Palindrome Check**: Compare string with its reverse
3. **Edge Cases**: Empty string, single character, special characters only

### 💭 **Initial Approach Ideas**

#### ❌ **Brute Force: String Preprocessing**
```python
def isPalindrome(self, s: str) -> bool:
    # Clean the string
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    # Check if palindrome
    return cleaned == cleaned[::-1]
```

**Issues:**
- ❌ **Space**: O(n) for creating new string
- ❌ **Time**: O(n) for string building + O(n) for reversal = O(n) but inefficient

---

## ✅ Optimal Solution: Two Pointers

### 💡 **Key Insight**: Check Characters In-Place!

Instead of preprocessing the entire string, check characters on-the-fly using two pointers.

```python
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right  
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
    
    return True
```

### 🎯 **Why This Works:**

| Step | Left Pointer | Right Pointer | Action |
|------|-------------|---------------|---------|
| 1 | Skip non-alphanumeric | Skip non-alphanumeric | Move inward |
| 2 | Compare `s[left].lower()` | Compare `s[right].lower()` | Check match |
| 3 | Move inward | Move inward | Continue |

---

## 🔍 Step-by-Step Walkthrough

### Example: `s = "A man, a plan, a canal: Panama"`

```
Initial: A   m a n ,   a   p l a n   a   c a n a l :   P a n a m a
Index:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
Left:    ^                                                                                        ^  Right

Step 1: left=0 ('A'), right=32 ('a') → 'a' == 'a' ✓
Step 2: left=1 ('m'), right=31 ('m') → 'm' == 'm' ✓  
Step 3: left=2 ('a'), right=30 ('a') → 'a' == 'a' ✓
...continue until pointers meet...

Result: All characters match → True
```

---

## ⚡ Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **String Building** | O(n) | O(n) | Creates new string |
| **Two Pointers** | **O(n)** | **O(1)** | In-place checking |

### 🔬 **Why O(n) Time?**
- Each character is visited **at most once**
- Skipping non-alphanumeric takes O(n) total across all iterations
- Character comparison is O(1)

---

## 🛠️ Alternative Approaches

### 📋 Approach 1: String Preprocessing + Comparison
```python
def isPalindrome(self, s: str) -> bool:
    # Using list comprehension + join (more efficient than concatenation)
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
```
- **Pros**: Simple and readable
- **Cons**: O(n) extra space

### 🔄 Approach 2: Recursive Two Pointers
```python
def isPalindrome(self, s: str) -> bool:
    def helper(left, right):
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        if left >= right:
            return True
        if s[left].lower() != s[right].lower():
            return False
        return helper(left + 1, right - 1)
    
    return helper(0, len(s) - 1)
```
- **Pros**: Elegant recursive structure
- **Cons**: O(n) space due to call stack

### 🎯 Approach 3: Regular Expressions
```python
import re

def isPalindrome(self, s: str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]
```
- **Pros**: Very concise
- **Cons**: Regex overhead, O(n) space

---

## 🧪 Edge Cases & Testing

| Input | Expected | Explanation |
|-------|----------|-------------|
| `""` | `True` | Empty string |
| `"a"` | `True` | Single character |
| `".,!@#"` | `True` | No alphanumeric chars |
| `"A"` | `True` | Single letter |
| `"Aa"` | `True` | Case insensitive |
| `"ab"` | `False` | Simple non-palindrome |

```python
# Test cases
test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True),
    ("a", True),
    ("Madam", True),
    ("No 'x' in Nixon", True),
    ("Mr. Owl ate my metal worm", True)
]
```

---

## 🎓 Key Takeaways

1. **🎯 Two Pointers Pattern**: Perfect for palindrome problems
2. **⚡ In-Place Processing**: Avoid creating new strings when possible
3. **🔍 Character Validation**: Use `isalnum()` for alphanumeric checking
4. **📝 Case Handling**: Always normalize case with `.lower()`
5. **🚀 Early Exit**: Return `False` immediately when mismatch found

## 🐛 Common Pitfalls

- ❌ Forgetting case-insensitive comparison
- ❌ Not handling special characters properly
- ❌ Off-by-one errors in pointer movement
- ❌ Not checking `left < right` in while loops
- ❌ Creating unnecessary intermediate strings

---

## 🔗 Related Problems

- [🔄 **#9 Palindrome Number**](../9/) - Palindrome without string conversion
- [📝 **#131 Palindrome Partitioning**](../131/) - Advanced palindrome techniques
- [🎯 **#234 Palindrome Linked List**](../234/) - Two pointers on linked lists
- [⚡ **#5 Longest Palindromic Substring**](../5/) - Dynamic programming approach
- [🔍 **#680 Valid Palindrome II**](../680/) - Palindrome with one deletion allowed

---

## 📚 Python String Methods Reference

```python
# Essential methods for this problem
char.isalnum()    # True if alphanumeric
char.isalpha()    # True if alphabetic  
char.isdigit()    # True if digit
char.lower()      # Convert to lowercase
char.upper()      # Convert to uppercase

# String slicing
s[::-1]          # Reverse string
s[start:end]     # Substring
```

## 🏆 Best Practices for Palindrome Problems

1. **Always consider two pointers** for O(1) space
2. **Handle edge cases** early (empty, single char)
3. **Normalize input** (case, special chars) consistently
4. **Use built-in methods** like `isalnum()` for clarity
5. **Test with various inputs** including edge cases