class Solution:

    def encode(self, strs: List[str]) -> str:
        ult = ""
        for i in strs:
            length = len(i)
            ult += str(length) + ":" + i
        return ult
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
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