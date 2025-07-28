class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isLast = False

    def addWord(self, word: str) -> None:
        for letter in word : 
            if letter not in self.children : 
                self.children[letter] = WordDictionary()
            
            self = self.children[letter]
        
        self.isLast = True
        return

    def search(self, word: str) -> bool:

        for index in range(0, len(word)) :

            if word[index] == ".":

                #for each child in the current level 
                for child in self.children :

                    if self.children[child].search(word[index+1:]): 
                        return True 
                    
                return False

            else : 
                if word[index] not in self.children: 
                    return False
                self = self.children[word[index]]
            
        return self.isLast

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)