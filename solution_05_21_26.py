class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = self.buildTrie(arr2)
        
        longest = 0
        for w in arr1:
            curlen = 0
            node = root
            for l in str(w):
                if l in node.children:
                    node = node.children[l]
                    curlen += 1
                else:
                    break
            longest = max(longest, curlen)


        return longest
        
    
    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in str(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
        return root
