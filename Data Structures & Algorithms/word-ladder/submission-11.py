class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nei = defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                nei[pattern].append(w)
            
        q = deque()
        n = 1
        visit = set()
        q.append(beginWord)
        visit.add(beginWord)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return n
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            n += 1
        return 0
