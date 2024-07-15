from functools import cache

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)

        adjList = collections.defaultdict(set)
        for i in wordList:
            for j in range(n):
                adjList[i[:j] + "*" + i[j+1:]].add(i)

        visited = set()
        ans = 0
        queue = [(0, beginWord)]

        while queue:
            seq_length, curr_word = queue.pop(0)

            if curr_word == endWord:
                return seq_length + 1

            if curr_word in visited:
                continue

            visited.add(curr_word)    

            for j in range(len(curr_word)):
                pattern = curr_word[:j] + "*" + curr_word[j+1:]
                for i in adjList[pattern]:
                    if i not in visited:
                        queue.append((seq_length + 1, i))
        
        return 0