class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for i in strs:
            sentence += str(len(i)) + "#" + i
        return sentence
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = ""
            while s[i] != "#":
                j += s[i]
                i+=1
            j = int(j)
            i+=1
            add_string = s[i:i+j]
            res.append(add_string)
            i = i+j
        return res
        