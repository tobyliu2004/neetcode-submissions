class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            length = len(i)
            res += str(length) + ":" + i
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            num = ""
            while s[i] != ":":
                num += s[i]
                i += 1
            number = int(num)
            i += 1
            word = ""
            for j in range(i, i+number):
                word += s[j]
                i += 1
            res.append(word)
        return res