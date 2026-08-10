class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        wordList.append(beginWord)
        track = defaultdict(list)
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + "." + word[i+1:]
                track[pattern].append(word)
        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "." + word[j+1:]
                    for neighbor in track[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0