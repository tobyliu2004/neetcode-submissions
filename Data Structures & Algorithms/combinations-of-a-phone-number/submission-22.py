class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
        res = []
        def dfs(i, cur):
            if i == len(digits):
                res.append(str("".join(cur.copy())))
                return
            for j in digitToChar[digits[i]]:
                cur.append(j)
                dfs(i+1, cur)
                cur.pop()
        if not digits:
            return []
        dfs(0,[])
        return res