class Solution:

    def encode(self, strs: List[str]) -> str:
        ultimate = ""
        for i in strs:
            length = len(i)
            ultimate += str(length) + ":" + i
        return ultimate
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            count = ""
            while s[i] != ":":
                count += s[i]
                i += 1
            wordCount = int(count)
            i += 1
            word = ""
            for n in range(wordCount):
                word += s[i]
                i += 1
            res.append(word)
        return res