class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        final = []
        while i < len(s):
            num = ""
            while s[i] != ":":
                num += s[i]
                i += 1
            number = int(num)
            i += 1
            word = ""
            for j in range(i, i+number):
                i += 1
                word += s[j]
            final.append(word)
        return final
            