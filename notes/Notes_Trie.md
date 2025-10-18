# Trie (Prefix Tree) Deep Dive 🌳

## Table of Contents
- [Core Concepts](#core-concepts)
- [Implementation Strategies](#implementation-strategies)
- [Common Patterns](#common-patterns)
- [Advanced Techniques](#advanced-techniques)
- [Problem-Solving Framework](#problem-solving-framework)
- [Time & Space Complexity](#time--space-complexity)
- [Common Pitfalls](#common-pitfalls)

## Core Concepts
<details>
<summary>Click to expand</summary>

### What is a Trie?
A **trie** (pronounced "try") is a tree-like data structure used to store and retrieve strings. Each node represents a character, and the path from root to any node spells out a word or prefix.

### Key Properties
1. **Character-based nodes**: Each node represents a single character
2. **Path spells words**: Root to node path forms a word/prefix
3. **Shared prefixes**: Common prefixes are shared between words
4. **Efficient lookups**: O(m) time where m is word length
5. **Prefix matching**: Natural support for prefix-based operations

### When to Use Tries
- **Autocomplete systems**: Find all words with given prefix
- **Spell checkers**: Check if word exists in dictionary
- **IP routing tables**: Longest prefix matching
- **Contact lists**: Search by name prefix
- **Text editors**: Word suggestions
</details>

## Implementation Strategies
<details>
<summary>Click to expand</summary>

### 1. Dictionary-Based Implementation
```python
class Trie:
    def __init__(self):
        self.children = {}  # Character -> Trie node
        self.is_end = False  # Marks complete words
    
    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### 2. Array-Based Implementation (for fixed character sets)
```python
class Trie:
    def __init__(self):
        self.children = [None] * 26  # For lowercase letters
        self.is_end = False
    
    def insert(self, word: str) -> None:
        node = self
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self
        for char in word:
            idx = ord(char) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end
```

### 3. Self Reassignment Pattern
```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word: str) -> None:
        for char in word:
            if char not in self.children:
                self.children[char] = Trie()
            self = self.children[char]  # Move down tree
        self.is_end = True
```
</details>

## Common Patterns
<details>
<summary>Click to expand</summary>

### 1. Basic Trie Operations
```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### 2. Word Search with Backtracking
```python
def find_words(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    def dfs(row, col, node, path):
        if node.is_end:
            result.add(''.join(path))
        
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = row + dr, col + dc
            if (0 <= nr < len(board) and 0 <= nc < len(board[0]) and
                board[nr][nc] in node.children):
                char = board[nr][nc]
                board[nr][nc] = '#'  # Mark as visited
                path.append(char)
                dfs(nr, nc, node.children[char], path)
                path.pop()
                board[nr][nc] = char  # Restore
    
    result = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in trie.children:
                char = board[i][j]
                board[i][j] = '#'
                dfs(i, j, trie.children[char], [char])
                board[i][j] = char
    
    return list(result)
```

### 3. Autocomplete Implementation
```python
def autocomplete(trie, prefix):
    node = trie
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]
    
    def collect_words(node, current_word):
        words = []
        if node.is_end:
            words.append(current_word)
        for char, child in node.children.items():
            words.extend(collect_words(child, current_word + char))
        return words
    
    return collect_words(node, prefix)
```

### 4. Longest Common Prefix
```python
def longest_common_prefix(words):
    if not words:
        return ""
    
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    node = trie
    prefix = []
    
    while len(node.children) == 1 and not node.is_end:
        char = list(node.children.keys())[0]
        prefix.append(char)
        node = node.children[char]
    
    return ''.join(prefix)
```
</details>

## Advanced Techniques
<details>
<summary>Click to expand</summary>

### 1. Compressed Trie (Radix Tree)
```python
class CompressedTrie:
    def __init__(self):
        self.children = {}  # prefix -> (Trie, remaining)
        self.is_end = False
    
    def insert(self, word: str) -> None:
        if not word:
            self.is_end = True
            return
        
        # Find common prefix with existing children
        for prefix, (child, remaining) in self.children.items():
            common = self._common_prefix(word, prefix)
            if common:
                if common == prefix:
                    # Word starts with existing prefix
                    child.insert(word[len(prefix):])
                else:
                    # Split existing node
                    new_child = CompressedTrie()
                    new_child.children[prefix[len(common):]] = (child, remaining)
                    new_child.insert(word[len(common):])
                    del self.children[prefix]
                    self.children[common] = (new_child, "")
                return
        
        # No common prefix found
        self.children[word] = (CompressedTrie(), "")
        self.children[word][0].is_end = True
    
    def _common_prefix(self, s1, s2):
        i = 0
        while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
            i += 1
        return s1[:i]
```

### 2. Suffix Trie
```python
class SuffixTrie:
    def __init__(self, text):
        self.root = Trie()
        self._build_suffix_trie(text)
    
    def _build_suffix_trie(self, text):
        for i in range(len(text)):
            suffix = text[i:]
            self._insert_suffix(suffix, i)
    
    def _insert_suffix(self, suffix, start_idx):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True
        node.start_indices = getattr(node, 'start_indices', []) + [start_idx]
    
    def search_pattern(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return []
            node = node.children[char]
        
        if node.is_end:
            return node.start_indices
        return []
```

### 3. Trie with Frequency Counting
```python
class FrequencyTrie:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0
    
    def insert(self, word: str, freq: int = 1) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = FrequencyTrie()
            node = node.children[char]
        node.is_end = True
        node.frequency += freq
    
    def get_top_k_words(self, prefix: str, k: int):
        node = self
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        def collect_words(node, current_word):
            words = []
            if node.is_end:
                words.append((current_word, node.frequency))
            for char, child in node.children.items():
                words.extend(collect_words(child, current_word + char))
            return words
        
        words = collect_words(node, prefix)
        words.sort(key=lambda x: x[1], reverse=True)
        return [word for word, freq in words[:k]]
```

### 4. Memory-Efficient Trie
```python
class MemoryEfficientTrie:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self._word_count = 0
    
    def insert(self, word: str) -> None:
        if not word:
            self.is_end = True
            self._word_count += 1
            return
        
        char = word[0]
        if char not in self.children:
            self.children[char] = MemoryEfficientTrie()
        self.children[char].insert(word[1:])
        self._word_count += 1
    
    def delete(self, word: str) -> bool:
        if not word:
            if self.is_end:
                self.is_end = False
                self._word_count -= 1
                return True
            return False
        
        char = word[0]
        if char not in self.children:
            return False
        
        if self.children[char].delete(word[1:]):
            self._word_count -= 1
            if self.children[char]._word_count == 0:
                del self.children[char]
            return True
        return False
```
</details>

## Problem-Solving Framework
<details>
<summary>Click to expand</summary>

### 1. Identify Trie Usage
**Use tries when you need:**
- String/word storage and retrieval
- Prefix-based operations
- Autocomplete functionality
- Pattern matching in text
- Efficient string lookups

### 2. Choose Implementation
- **Dictionary-based**: Flexible, works with any character set
- **Array-based**: Space-efficient for fixed character sets (e.g., lowercase letters)
- **Self-reassignment**: Clean traversal pattern

### 3. Design Operations
- **Insert**: Traverse path, create nodes as needed, mark end
- **Search**: Traverse path, check if complete word exists
- **Prefix**: Traverse path, check if prefix exists
- **Delete**: Traverse path, remove nodes if no other words use them

### 4. Handle Edge Cases
- Empty strings
- Non-existent words/prefixes
- Duplicate insertions
- Memory cleanup for deletions
</details>

## Related Problems
<details>
<summary>Click to expand</summary>

### Easy
- [208. Implement Trie (Prefix Tree)](../208/README.md) - Basic trie implementation

### Medium
- [211. Design Add and Search Words Data Structure](#) *(if available)* - Trie with wildcard support
- [212. Word Search II](#) *(if available)* - Trie + backtracking
- [648. Replace Words](#) *(if available)* - Trie for prefix replacement

### Hard
- [745. Prefix and Suffix Search](#) *(if available)* - Advanced trie with suffix support
- [1032. Stream of Characters](#) *(if available)* - Trie for streaming data
</details>

## Time & Space Complexity
<details>
<summary>Click to expand</summary>

### Trie Operations
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(1) |
| startsWith | O(m) | O(1) |
| Delete | O(m) | O(1) |

Where m = length of the word/prefix

### Space Analysis
- **Dictionary-based**: O(ALPHABET_SIZE × N × M) where N = number of words, M = average word length
- **Array-based**: O(ALPHABET_SIZE × N × M) but more predictable
- **Compressed**: O(N × M) in best case, O(ALPHABET_SIZE × N × M) in worst case

### Memory Optimization
- Use compressed tries for large datasets
- Implement lazy deletion for dynamic datasets
- Consider array-based implementation for fixed character sets
</details>

## Common Pitfalls & Best Practices
<details>
<summary>Click to expand</summary>

### ❌ Common Mistakes

1. **Forgetting to Mark Word Endings**
   ```python
   # Wrong: Can't distinguish between "app" and "apple"
   def insert(self, word):
       for char in word:
           # ... create nodes
       # Missing: self.is_end = True
   
   # Correct
   def insert(self, word):
       for char in word:
           # ... create nodes
       self.is_end = True  # Mark complete word
   ```

2. **Not Handling Empty Strings**
   ```python
   # Wrong: Doesn't handle empty string
   def search(self, word):
       for char in word:  # Fails for ""
           # ...
   
   # Correct
   def search(self, word):
       if not word:
           return self.is_end
       # ... rest of logic
   ```

3. **Inefficient Traversal**
   ```python
   # Wrong: Creating unnecessary variables
   def startsWith(self, prefix):
       current = self
       for char in prefix:
           if char not in current.children:
               return False
           current = current.children[char]
       return True
   
   # Better: Self reassignment
   def startsWith(self, prefix):
       for char in prefix:
           if char not in self.children:
               return False
           self = self.children[char]
       return True
   ```

### ✅ Best Practices

1. **Use Self Reassignment for Clean Traversal**
   ```python
   def insert(self, word):
       for char in word:
           if char not in self.children:
               self.children[char] = Trie()
           self = self.children[char]  # Clean traversal
       self.is_end = True
   ```

2. **Separate Search and startsWith Logic**
   ```python
   def search(self, word):
       # Must be complete word
       node = self._get_node(word)
       return node and node.is_end
   
   def startsWith(self, prefix):
       # Just need prefix to exist
       return self._get_node(prefix) is not None
   
   def _get_node(self, word):
       node = self
       for char in word:
           if char not in node.children:
               return None
           node = node.children[char]
       return node
   ```

3. **Handle Edge Cases Properly**
   ```python
   def insert(self, word):
       if not word:
           self.is_end = True
           return
       # ... rest of logic
   ```

4. **Use Appropriate Data Structures**
   ```python
   # For fixed character sets (lowercase letters)
   self.children = [None] * 26
   
   # For flexible character sets
   self.children = {}
   ```

5. **Implement Memory-Efficient Deletion**
   ```python
   def delete(self, word):
       if not word:
           if self.is_end:
               self.is_end = False
               return True
           return False
       
       char = word[0]
       if char not in self.children:
           return False
       
       if self.children[char].delete(word[1:]):
           if not self.children[char].children and not self.children[char].is_end:
               del self.children[char]
           return True
       return False
   ```
</details>

## Additional Resources
<details>
<summary>Click to expand</summary>

1. [Trie Data Structure Visualization](https://visualgo.net/en/trie)
2. [Trie Applications in Computer Science](https://en.wikipedia.org/wiki/Trie)
3. [Advanced Trie Patterns](https://leetcode.com/tag/trie/)
4. [Compressed Trie (Radix Tree)](https://en.wikipedia.org/wiki/Radix_tree)
</details>

---

*Remember: Tries are perfect for string-based problems, especially those involving prefixes. The key insight is that each node represents a character, and the path from root to node spells out a word or prefix. Master the self-reassignment pattern for clean traversal!* 