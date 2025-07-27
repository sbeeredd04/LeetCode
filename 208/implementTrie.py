class Trie:

    def __init__(self):
        self.letters = {}
        self.isLast = False

    def insert(self, word: str) -> None:
        
        for letter in word : 
            if letter not in self.letters :
                self.letters[letter] = Trie()       #letter does not exist create a new trie and move

            self = self.letters[letter]             #move to next node
        
        self.isLast = True                          #mark the last node as the end of the word

    def search(self, word: str) -> bool:
        
        for letter in word : 
            if letter not in self.letters :     #if the letter not in the dict then word does not exist
                return False
            
            self = self.letters[letter]         #move the node
        
        return self.isLast                      #word exists if the node is islast

    def startsWith(self, prefix: str) -> bool:
        "same algorithm as search but no need to check for last word"
        
        for letter in prefix :                  
            if letter not in self.letters : 
                return False
            
            self = self.letters[letter]

        return True

    # DEBUG VERSION: Detailed trie operations tracking
    def insert_debug(self, word: str) -> None:
        """Debug version of insert with detailed state tracking"""
        print(f"\nINSERTING: '{word}'")
        print(f"Starting at root node")
        
        current = self
        path = []
        
        for i, letter in enumerate(word):
            print(f"  Step {i+1}: Processing letter '{letter}'")
            print(f"    Current node letters: {list(current.letters.keys())}")
            
            if letter not in current.letters:
                print(f"    Letter '{letter}' not found - creating new node")
                current.letters[letter] = Trie()
            else:
                print(f"    Letter '{letter}' found - moving to existing node")
            
            current = current.letters[letter]
            path.append(letter)
            print(f"    Path so far: {''.join(path)}")
            print(f"    Moved to node with letters: {list(current.letters.keys())}")
        
        print(f"  Marking end of word: '{word}'")
        current.isLast = True
        print(f"  Final path: {' -> '.join(path)}")
        print(f"  Word '{word}' inserted successfully!")

    def search_debug(self, word: str) -> bool:
        """Debug version of search with detailed state tracking"""
        print(f"\nSEARCHING: '{word}'")
        print(f"Starting at root node")
        
        current = self
        path = []
        
        for i, letter in enumerate(word):
            print(f"  Step {i+1}: Looking for letter '{letter}'")
            print(f"    Current node letters: {list(current.letters.keys())}")
            
            if letter not in current.letters:
                print(f"    Letter '{letter}' not found - word doesn't exist")
                print(f"    SEARCH RESULT: False")
                return False
            
            print(f"    Letter '{letter}' found - moving to next node")
            current = current.letters[letter]
            path.append(letter)
            print(f"    Path so far: {''.join(path)}")
            print(f"    Current node isLast: {current.isLast}")
        
        result = current.isLast
        print(f"  Reached end of word")
        print(f"  Final path: {' -> '.join(path)}")
        print(f"  isLast flag: {result}")
        print(f"  SEARCH RESULT: {result}")
        return result

    def startsWith_debug(self, prefix: str) -> bool:
        """Debug version of startsWith with detailed state tracking"""
        print(f"\nSTARTSWITH: '{prefix}'")
        print(f"Starting at root node")
        
        current = self
        path = []
        
        for i, letter in enumerate(prefix):
            print(f"  Step {i+1}: Looking for letter '{letter}'")
            print(f"    Current node letters: {list(current.letters.keys())}")
            
            if letter not in current.letters:
                print(f"    Letter '{letter}' not found - prefix doesn't exist")
                print(f"    STARTSWITH RESULT: False")
                return False
            
            print(f"    Letter '{letter}' found - moving to next node")
            current = current.letters[letter]
            path.append(letter)
            print(f"    Path so far: {''.join(path)}")
        
        print(f"  Reached end of prefix")
        print(f"  Final path: {' -> '.join(path)}")
        print(f"  STARTSWITH RESULT: True")
        return True

    def print_trie_structure(self, prefix="", is_last=True):
        """Print the trie structure for visualization"""
        if self.isLast:
            print(f"{prefix}└── [END]")
        else:
            print(f"{prefix}├──")
        
        for i, (letter, child) in enumerate(self.letters.items()):
            is_last_child = i == len(self.letters) - 1
            child_prefix = prefix + ("    " if is_last else "│   ")
            print(f"{prefix}{'└──' if is_last_child else '├──'} '{letter}'")
            child.print_trie_structure(child_prefix, is_last_child)

    def test_debug(self):
        """Test all operations with debugging"""
        print("="*60)
        print("TESTING TRIE IMPLEMENTATION WITH DEBUG")
        print("="*60)
        
        # Test insertions
        self.insert_debug("apple")
        self.insert_debug("app")
        self.insert_debug("banana")
        
        print("\n" + "="*40)
        print("TRIE STRUCTURE:")
        print("="*40)
        self.print_trie_structure()
        
        # Test searches
        self.search_debug("apple")  # Should return True
        self.search_debug("app")    # Should return True  
        self.search_debug("banana") # Should return True
        self.search_debug("ban")    # Should return False
        self.search_debug("applee") # Should return False
        
        # Test startsWith
        self.startsWith_debug("app")   # Should return True
        self.startsWith_debug("ban")   # Should return True
        self.startsWith_debug("c")     # Should return False
        self.startsWith_debug("appl")  # Should return True