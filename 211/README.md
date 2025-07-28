# Design Add and Search Words Data Structure - LeetCode 211

## Problem Statement
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds word to the data structure, it can be matched later.
- `bool search(word)` Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

**Example:**
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## Initial Approach & Intuition

> **"This is a trie problem with a wildcard twist! The key insight is that when I encounter a dot '.', I need to try ALL possible characters at that position. This is essentially a DFS problem where I explore all possible paths when I hit a wildcard. The tricky part was getting the recursion right - I had to make sure I return False only after trying ALL children when I hit a dot, and I had to handle the case where I reach the end of the word but the current node isn't marked as a complete word."**

## Initial Hunch and Hints

<details>
<summary>► My First Thoughts</summary>

When I first saw this problem, my immediate thought was:
> "This is like a trie but with wildcards! I need to build a trie structure and when searching, if I hit a dot, I have to try all possible characters at that level."

My initial approach was:
1. **Build a trie structure** - similar to regular trie implementation
2. **Handle dots as wildcards** - when searching, if current char is '.', try all children
3. **Use DFS for wildcard matching** - recursively search all possible paths
4. **Track word endings** - use isLast flag to distinguish complete words from prefixes

The key challenge was getting the recursion logic right - I had to make sure I explored all possibilities when hitting a dot and handled the base cases correctly.
</details>

<details>
<summary>▲ Key Insights That Helped</summary>

- **Trie with wildcards**: The basic structure is a trie, but search needs to handle '.' as any character
- **DFS for wildcard matching**: When I hit a '.', I need to recursively try all children
- **Return False after trying all children**: Don't return False immediately when hitting a dot, try all possibilities first
- **Check isLast at the end**: Only return True if I've processed the entire word AND reached a complete word
- **Handle empty word case**: If word is empty, check if current node is marked as complete word
</details>

<details>
<summary>⚠ Common Pitfalls I Avoided</summary>

- **Returning False too early**: When hitting a dot, I need to try ALL children before returning False
- **Not checking isLast**: Must verify the current node represents a complete word, not just a prefix
- **Wrong recursion structure**: The recursion needs to handle the remaining substring correctly
- **Missing base case**: Need to handle the case where word is empty but node isn't marked as complete
- **Confusing search logic**: The order of checks matters - handle dots first, then regular characters
</details>

## My Solution Analysis

### What I Implemented:
```python
class WordDictionary:
    def __init__(self):
        self.children = {}
        self.isLast = False

    def addWord(self, word: str) -> None:
        for letter in word: 
            if letter not in self.children: 
                self.children[letter] = WordDictionary()
            self = self.children[letter]
        self.isLast = True
        return

    def search(self, word: str) -> bool:
        for index in range(0, len(word)):
            if word[index] == ".":
                # Try all children when hitting a dot
                for child in self.children:
                    if self.children[child].search(word[index+1:]): 
                        return True 
                return False  # No child matched
            else: 
                if word[index] not in self.children: 
                    return False
                self = self.children[word[index]]
        
        return self.isLast  # Must be complete word
```

### Key Design Decisions:

**1. Trie Structure with Wildcard Support**
- Standard trie implementation for storing words
- Special handling for '.' character during search
- DFS approach to explore all possible matches

**2. Wildcard Handling Strategy**
```python
if word[index] == ".":
    for child in self.children:
        if self.children[child].search(word[index+1:]): 
            return True 
    return False  # No child matched
```
When hitting a dot, try all possible characters at current level.

**3. Complete Word Verification**
```python
return self.isLast  # Must be complete word
```
Only return True if we've processed the entire word AND reached a node marked as complete word.

## Algorithm Analysis with Debugging

Let me trace through the algorithm with detailed debugging to show how it works:

### Debug Execution Trace:

**Adding words: "bad", "dad", "mad"**
```
ADDING: 'bad'
Step 1: 'b' not found → create new node → move to 'b' node
Step 2: 'a' not found → create new node → move to 'a' node  
Step 3: 'd' not found → create new node → move to 'd' node
Mark end of word: 'bad'

ADDING: 'dad'
Step 1: 'd' not found → create new node → move to 'd' node
Step 2: 'a' not found → create new node → move to 'a' node
Step 3: 'd' not found → create new node → move to 'd' node
Mark end of word: 'dad'

ADDING: 'mad'
Step 1: 'm' not found → create new node → move to 'm' node
Step 2: 'a' not found → create new node → move to 'a' node
Step 3: 'd' not found → create new node → move to 'd' node
Mark end of word: 'mad'
```

**Searching: "pad"**
```
SEARCHING: 'pad'
Step 1: 'p' not in children → return False
Result: False
```

**Searching: "bad"**
```
SEARCHING: 'bad'
Step 1: 'b' found → move to 'b' node
Step 2: 'a' found → move to 'a' node
Step 3: 'd' found → move to 'd' node
Check isLast: True
Result: True
```

**Searching: ".ad"**
```
SEARCHING: '.ad'
Step 1: '.' found → try all children
  - Try 'b': search('ad') on 'b' node
    - 'a' found → move to 'a' node
    - 'd' found → move to 'd' node
    - Check isLast: True → return True
  - Return True (found match)
Result: True
```

**Searching: "b.."**
```
SEARCHING: 'b..'
Step 1: 'b' found → move to 'b' node
Step 2: '.' found → try all children
  - Try 'a': search('.') on 'a' node
    - '.' found → try all children
      - Try 'd': search('') on 'd' node
        - Check isLast: True → return True
    - Return True (found match)
  - Return True (found match)
Result: True
```

## Algorithm Flow Diagram

Based on the debug execution trace, here's the detailed search algorithm:

```mermaid
flowchart TD
    A[Start Search: word, current_node] --> B{word empty?}
    B -->|Yes| C{current_node.isLast?}
    C -->|Yes| D[Return True]
    C -->|No| E[Return False]
    
    B -->|No| F{current_char == '.'?}
    F -->|Yes| G[For each child in current_node.children]
    G --> H[Recursive search: word[1:], child_node]
    H --> I{Recursive search returned True?}
    I -->|Yes| J[Return True]
    I -->|No| K{More children to try?}
    K -->|Yes| G
    K -->|No| L[Return False - no children matched]
    
    F -->|No| M{current_char in current_node.children?}
    M -->|No| N[Return False - char not found]
    M -->|Yes| O[Move to child node: current_node = current_node.children[current_char]]
    O --> P[Continue with word[1:]]
    P --> B
    
    style D fill:#90EE90
    style J fill:#90EE90
    style L fill:#FFB6C1
    style N fill:#FFB6C1
    style E fill:#FFB6C1
```

### Key Execution Points:
- **Regular character**: Move to child node if exists, return False if not
- **Dot character**: Try all children recursively, return True if any match
- **End of word**: Check if current node is marked as complete word
- **No children match**: Return False after trying all possibilities

## Self-Reflection: What I Did and Learned

### ▲ What I Did Well

**1. Recognized the Pattern Immediately**
I quickly identified this as a trie problem with wildcard matching. My intuition about "trie with wildcards" was spot on, and I understood that dots require exploring all possible paths.

**2. Implemented DFS Correctly**
The key insight was using DFS to explore all possible matches when hitting a dot. I correctly implemented the recursive search that tries all children when encountering a wildcard.

**3. Handled Edge Cases Properly**
I made sure to:
- Return False only after trying ALL children when hitting a dot
- Check `isLast` flag to ensure complete word matches
- Handle the case where word is empty but node isn't marked as complete

**4. Got the Recursion Structure Right**
The recursion logic was tricky, but I got it right:
```python
if word[index] == ".":
    for child in self.children:
        if self.children[child].search(word[index+1:]): 
            return True 
    return False  # No child matched
```

### ▼ What I Struggled With

**1. Initial Logic Errors**
My first attempts had several issues:
- I was returning False too early when hitting dots
- I wasn't checking `isLast` properly at the end
- I had the wrong order of conditions in the search method

**2. Recursion Base Cases**
I initially struggled with:
- When to return True vs False
- How to handle empty words
- Making sure I explored all possibilities before giving up

**3. Understanding the Problem Requirements**
I had to think carefully about:
- What constitutes a "match" (complete word vs prefix)
- How dots should behave (match any single character)
- When to stop searching (after processing entire word)

### ■ Problem-Solving Process That Worked

**Step 1: Understand the Data Structure**
- "This is a trie with wildcard support"
- "Dots match any single character"
- "I need to explore all possible paths when hitting a dot"

**Step 2: Design the Search Algorithm**
- "Regular characters: move to child if exists"
- "Dot characters: try all children recursively"
- "End of word: check if current node is complete word"

**Step 3: Handle Edge Cases**
- "Return False only after trying all children for dots"
- "Check isLast flag for complete word verification"
- "Handle empty word case properly"

### ► What I'd Do Differently Next Time

**1. Start with Simple Examples**
I should have drawn out the trie structure with a few simple words first to visualize how the search would work.

**2. Test Edge Cases Early**
I should have tested these cases right away:
- Words with multiple dots
- Dots at the beginning, middle, and end
- Words that are prefixes of other words
- Empty words and single characters

**3. Add More Debug Output**
The debug version I created was really helpful - I should add debugging capabilities to understand the recursion flow better.

**4. Consider Performance Optimization**
For large-scale applications, I might want to consider:
- Caching search results
- Optimizing the trie structure
- Handling very long words efficiently

### ◆ Key Insights I'll Remember

**1. DFS for Wildcard Matching**
```python
if char == '.':
    for child in children:
        if search(remaining_word, child):
            return True
    return False
```
This pattern is crucial for any wildcard matching problem.

**2. Complete Word Verification**
```python
return self.isLast  # Must be complete word
```
Always check if you've reached a complete word, not just a prefix.

**3. Try All Possibilities Before Giving Up**
When dealing with wildcards or multiple paths, make sure to explore all options before returning False.

**4. Recursion Base Cases**
- Empty word: check if current node is complete word
- No matching character: return False
- Dot character: try all children before giving up

### ▲ How This Problem Helped Me Grow

**Recursion Skills:** I'm getting better at designing recursive algorithms with proper base cases  
**Wildcard Pattern Matching:** I now understand how to handle flexible matching patterns  
**Trie Data Structure:** I'm more comfortable with trie implementations and traversals  
**Debugging Complex Logic:** I'm learning to trace through recursive algorithms step by step  

### ★ What I'm Proud Of

My final solution is clean, efficient, and handles all the edge cases correctly! I particularly like:
- The DFS approach for wildcard matching
- The proper handling of the `isLast` flag
- The correct recursion structure that explores all possibilities
- The clean separation between regular character and wildcard handling

The debug output shows the algorithm working perfectly - it correctly handles dots at any position, distinguishes between complete words and prefixes, and efficiently explores all possible matches.

### ➤ Next Steps for Improvement

1. **Practice more wildcard matching problems** to reinforce the DFS pattern
2. **Learn about regex implementations** and how they handle wildcards
3. **Explore trie optimizations** like compressed tries and suffix trees
4. **Practice recursive algorithm design** with proper base case handling
5. **Study pattern matching algorithms** like KMP, Boyer-Moore, and regex engines

This wildcard trie implementation was really satisfying to build! It's a perfect example of how combining data structures (trie) with algorithms (DFS) can solve complex pattern matching problems. The key insight about trying all children when hitting a dot is elegant and powerful.

---

**Time Complexity:** O(26^m) worst case for search where m is word length (due to wildcards)  
**Space Complexity:** O(n) where n is total number of characters in all words  
**Pattern:** Trie Data Structure with DFS Wildcard Matching
