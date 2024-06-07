class Trie:

    def __init__(self):
        self.tree = {"next": {}}

    def insert(self, word: str) -> None:
        last = self.tree["next"]
        for letter in word: 
            if letter in last:
                last = last[letter]["next"]
            else:
                last[letter] = {"next": {}}
                last = last[letter]["next"]

        last["word"] = True

    def search(self, word: str) -> str:
        last = self.tree["next"]
        root = ''
        for letter in word: 
            if letter in last:
                root += letter
                last = last[letter]["next"]

                if "word" in last and last["word"]:
                    return root
            else:
                return word 
    
        return word 

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        return ' '.join(map(trie.search, sentence.split(" ")))