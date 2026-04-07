class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open < n
        #only add close if closed < open
        # valid if open = closed = n
        per = []
        res = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(per))
                return
            if openN<n:
                per.append("(")
                backtrack(openN + 1, closeN)
                per.pop()
            if closeN<openN:
                per.append(")")
                backtrack(openN,closeN + 1)
                per.pop()
        backtrack(0,0)
        return res