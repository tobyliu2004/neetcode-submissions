class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for i in strs:
            sentence += i + "~"
        return sentence
    def decode(self, s: str) -> List[str]:
        words = s.split("~")
        words.pop()
        return words