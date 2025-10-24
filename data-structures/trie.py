"""
Trie (Prefix Tree) Implementation
A space-efficient data structure for string operations like autocomplete,
spell checking, and IP routing.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie data structure for efficient string operations.
    
    Time Complexity:
        - Insert: O(m) where m is the length of the word
        - Search: O(m)
        - StartsWith: O(m)
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """Search for a complete word in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word in the trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "application", "apricot", "banana"]
    
    for word in words:
        trie.insert(word)
    
    print(f"Search 'app': {trie.search('app')}")  # True
    print(f"Search 'appl': {trie.search('appl')}")  # False
    print(f"Starts with 'app': {trie.starts_with('app')}")  # True
    print(f"Starts with 'ban': {trie.starts_with('ban')}")  # True
