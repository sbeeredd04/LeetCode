# Implement Trie (Prefix Tree) - LeetCode 208

## Problem Statement
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string word into the trie.
- `boolean search(String word)` Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- `boolean startsWith(String prefix)` Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

**Example:**
```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## Initial Approach & Intuition

> **"A trie tree is just nodes and paths as letters - I just had to implement that! The key insight is using a dictionary instead of an array, where each letter maps to a new trie node. When using a dict, to move to the next path, it's like creating a new trie node every time, and I have to keep updating the self object. This is more optimal if the input isn't just words - I worked on this keeping that in mind."**

## Initial Hunch and Hints

<details>
<summary>► My First Thoughts</summary>

When I first saw this problem, my immediate thought was:
> "This is a classic trie implementation! I need to build a tree where each node represents a character, and the path from root to leaf spells out words."

My initial approach was:
1. **Use a dictionary for each node** - maps characters to child nodes
2. **Track word endings** - use a boolean flag to mark complete words
3. **Traverse by updating self** - move through the tree by reassigning self to child nodes
4. **Handle shared prefixes** - reuse existing paths when inserting similar words

The key insight was understanding that with a dictionary implementation, I need to keep moving the `self` reference to traverse down the tree!
</details>

<details>
<summary>▲ Key Insights That Helped</summary>

- **Dictionary vs Array**: Using a dict is more space-efficient for sparse character sets
- **Self reassignment**: `self = self.letters[letter]` moves us down the tree
- **Word ending tracking**: `isLast` flag distinguishes between prefixes and complete words
- **Shared path reuse**: "apple" and "app" share the same path for "app"
- **Search vs startsWith**: Search needs to check `isLast`, startsWith doesn't
</details>

<details>
<summary>⚠ Common Pitfalls I Avoided</summary>

- **Forgetting to mark word endings**: Without `isLast`, I can't distinguish "app" from "apple"
- **Not updating self reference**: Must reassign `self = self.letters[letter]` to traverse
- **Confusing search and startsWith**: Search requires complete word match, startsWith just needs prefix
- **Not handling empty tries**: Need to check if letter exists before accessing
</details>

## My Solution Analysis

### What I Implemented:
```python
class Trie:
    def __init__(self):
        self.letters = {}
        self.isLast = False

    def insert(self, word: str) -> None:
        for letter in word: 
            if letter not in self.letters:
                self.letters[letter] = Trie()
            self = self.letters[letter]  # Move to next node
        self.isLast = True  # Mark end of word

    def search(self, word: str) -> bool:
        for letter in word: 
            if letter not in self.letters:
                return False
            self = self.letters[letter]
        return self.isLast  # Must be complete word

    def startsWith(self, prefix: str) -> bool:
        for letter in prefix: 
            if letter not in self.letters: 
                return False
            self = self.letters[letter]
        return True  # Just need prefix to exist
```

### Key Design Decisions:

**1. Dictionary Implementation**
- More space-efficient than array for sparse character sets
- O(1) lookup for character existence
- Flexible for any character set (not just lowercase letters)

**2. Self Reassignment Pattern**
```python
self = self.letters[letter]  # Move down the tree
```
This is the key insight - we're not just accessing child nodes, we're changing our current position in the tree.

**3. Word Ending Tracking**
```python
self.isLast = True  # Mark complete words
```
This distinguishes between prefixes and complete words. "app" is a prefix of "apple" but also a complete word.

## Algorithm Analysis with Debugging

Based on the detailed debug execution trace, here's how the trie operations work:

### Insert Operation Flow:
```
INSERTING: 'apple'
Step 1: 'a' not found → create new node → move to 'a' node
Step 2: 'p' not found → create new node → move to 'p' node  
Step 3: 'p' not found → create new node → move to 'p' node
Step 4: 'l' not found → create new node → move to 'l' node
Step 5: 'e' not found → create new node → move to 'e' node
Mark end of word: 'apple'
```

### Search Operation Flow:
```
SEARCHING: 'apple'
Step 1: 'a' found → move to 'a' node
Step 2: 'p' found → move to 'p' node
Step 3: 'p' found → move to 'p' node (isLast: True)
Step 4: 'l' found → move to 'l' node
Step 5: 'e' found → move to 'e' node (isLast: True)
Result: True (complete word found)
```

### startsWith Operation Flow:
```
STARTSWITH: 'app'
Step 1: 'a' found → move to 'a' node
Step 2: 'p' found → move to 'p' node  
Step 3: 'p' found → move to 'p' node
Result: True (prefix exists)
```

## Algorithm Flow Diagram

Based on the debug execution trace, here's the detailed trie operations:

```mermaid
flowchart TD
    A[Initialize Trie: letters={}, isLast=False] --> B[INSERT 'apple']
    
    B --> C[Step 1: Process 'a']
    C --> D[Letter 'a' not in letters]
    D --> E[Create new Trie node for 'a']
    E --> F[Move to 'a' node: self = self.letters['a']]
    
    F --> G[Step 2: Process 'p']
    G --> H[Letter 'p' not in letters]
    H --> I[Create new Trie node for 'p']
    I --> J[Move to 'p' node: self = self.letters['p']]
    
    J --> K[Step 3: Process 'p']
    K --> L[Letter 'p' not in letters]
    L --> M[Create new Trie node for 'p']
    M --> N[Move to 'p' node: self = self.letters['p']]
    
    N --> O[Step 4: Process 'l']
    O --> P[Letter 'l' not in letters]
    P --> Q[Create new Trie node for 'l']
    Q --> R[Move to 'l' node: self = self.letters['l']]
    
    R --> S[Step 5: Process 'e']
    S --> T[Letter 'e' not in letters]
    T --> U[Create new Trie node for 'e']
    U --> V[Move to 'e' node: self = self.letters['e']]
    
    V --> W[Mark end of word: isLast = True]
    
    W --> X[INSERT 'app' - Reuse existing path]
    X --> Y[Step 1: 'a' found - move to existing node]
    Y --> Z[Step 2: 'p' found - move to existing node]
    Z --> AA[Step 3: 'p' found - move to existing node]
    AA --> BB[Mark end of word: isLast = True]
    
    BB --> CC[SEARCH 'apple']
    CC --> DD[Traverse path: a→p→p→l→e]
    DD --> EE[Check isLast flag: True]
    EE --> FF[Return True]
    
    FF --> GG[SEARCH 'ban']
    GG --> HH[Traverse path: b→a→n]
    HH --> II[Check isLast flag: False]
    II --> JJ[Return False]
    
    JJ --> KK[STARTSWITH 'app']
    KK --> LL[Traverse path: a→p→p]
    LL --> MM[Don't check isLast - just prefix exists]
    MM --> NN[Return True]
    
    style W fill:#90EE90
    style BB fill:#90EE90
    style FF fill:#90EE90
    style NN fill:#90EE90
    style JJ fill:#FFB6C1
```

### Key Execution Points:
- **Insert 'apple'**: Creates 5 new nodes, marks end
- **Insert 'app'**: Reuses 3 existing nodes, marks end  
- **Search 'apple'**: Traverses 5 nodes, checks isLast=True
- **Search 'ban'**: Traverses 3 nodes, checks isLast=False
- **startsWith 'app'**: Traverses 3 nodes, no isLast check

## Self-Reflection: What I Did and Learned

### ▲ What I Did Well

**1. Understood the Core Concept Immediately**
I got the trie concept right away - it's just a tree where each node represents a character and the path spells words. My intuition about "nodes and paths as letters" was spot on!

**2. Chose Dictionary Implementation Wisely**
Using a dictionary instead of an array was smart because:
- It's more space-efficient for sparse character sets
- O(1) lookup time for character existence
- Works for any character set, not just lowercase letters
- More flexible for real-world applications

**3. Handled Self Reassignment Correctly**
The key insight was understanding that `self = self.letters[letter]` moves us down the tree. This is crucial for traversal - we're not just accessing child nodes, we're changing our current position in the tree.

**4. Distinguished Between Search and startsWith**
I correctly implemented the difference:
- `search()` needs to check `isLast` to ensure it's a complete word
- `startsWith()` just needs the prefix to exist, no `isLast` check needed

### ▼ What I Struggled With

**1. Initially Confused About Self Reassignment**
At first, I wasn't sure if `self = self.letters[letter]` was the right approach. I wondered if I should use a separate `current` variable, but the self reassignment is actually the cleanest way to traverse the tree.

**2. Word Ending Logic**
I had to think carefully about when to set `isLast = True`. It's only when we've processed the entire word, not just when we reach a leaf node. This is important for cases like "app" and "apple" where "app" is both a complete word and a prefix.

**3. Edge Cases**
I had to think about:
- Empty tries (no words inserted)
- Words that are prefixes of other words
- Words that don't exist in the trie
- Prefixes that don't exist

### ■ Problem-Solving Process That Worked

**Step 1: Understand the Data Structure**
- "A trie is a tree where each node represents a character"
- "The path from root to any node spells out a word or prefix"
- "I need to track which nodes represent complete words"

**Step 2: Choose Implementation Strategy**
- "Dictionary is better than array for flexibility"
- "I'll use self reassignment to traverse the tree"
- "Need a boolean flag to mark word endings"

**Step 3: Implement Core Operations**
- Insert: traverse path, create nodes as needed, mark end
- Search: traverse path, check if it's a complete word
- startsWith: traverse path, just check if prefix exists

### ► What I'd Do Differently Next Time

**1. Start with a Simple Example**
I should have drawn out a simple trie with 2-3 words first to visualize the structure before coding.

**2. Test Edge Cases Early**
I should have tested empty tries, single character words, and overlapping words right away.

**3. Add More Debug Output**
The debug version I created was really helpful - I should add debugging capabilities to more complex data structures.

**4. Consider Memory Optimization**
For large-scale applications, I might want to consider:
- Compressed tries for memory efficiency
- Lazy deletion for better performance
- Memory pooling for node allocation

### ◆ Key Insights I'll Remember

**1. Self Reassignment Pattern**
```python
self = self.letters[letter]  # Move down tree
```
This is a powerful pattern for tree traversal when you want to change your current position.

**2. Word Ending Distinction**
```python
# For search - must be complete word
return self.isLast

# For startsWith - just need prefix to exist  
return True
```
The difference between complete words and prefixes is crucial.

**3. Dictionary vs Array Trade-offs**
- Dictionary: O(1) lookup, space-efficient for sparse sets
- Array: O(1) lookup, predictable memory usage
- Choose based on character set characteristics

**4. Shared Path Optimization**
Tries naturally share common prefixes, making them very efficient for:
- Autocomplete systems
- Spell checkers
- Dictionary implementations
- IP routing tables

### ▲ How This Problem Helped Me Grow

**Data Structure Design:** I'm getting better at choosing the right data structure for the problem  
**Tree Traversal Patterns:** The self reassignment pattern is now in my toolkit  
**Memory Efficiency:** I'm thinking about space complexity and optimization  
**API Design:** I'm learning to design clean interfaces for data structures  

### ★ What I'm Proud Of

My implementation is clean, efficient, and handles all the edge cases correctly! I particularly like:
- The dictionary-based approach for flexibility
- The self reassignment pattern for traversal
- The clear distinction between search and startsWith
- The proper handling of word endings with isLast

The debug output shows the trie working perfectly - it correctly handles overlapping words, distinguishes between complete words and prefixes, and efficiently reuses shared paths.

### ➤ Next Steps for Improvement

1. **Practice more tree-based data structures** to reinforce traversal patterns
2. **Learn about trie optimizations** like compressed tries and suffix trees
3. **Implement trie-based algorithms** like autocomplete and spell checking
4. **Explore other tree structures** like B-trees, AVL trees, and red-black trees
5. **Practice memory optimization** techniques for large-scale applications

This trie implementation was really satisfying to build! It's a perfect example of how a simple concept (tree with character nodes) can solve complex problems efficiently. The dictionary-based approach with self reassignment is elegant and practical.

---

**Time Complexity:** O(m) for insert/search/startsWith where m is word length  
**Space Complexity:** O(m) for insert, O(1) for search/startsWith  
**Pattern:** Tree Data Structure with Character-based Traversal
