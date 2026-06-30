class Solution:
    def generateParenthesis(self, input_n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_n, closed_n):
            print(f"open_n: {open_n}, closed_n: {closed_n}")
            if open_n == closed_n == input_n:
                print(stack)
                res.append("".join(stack))
                return
            
            if open_n < input_n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()
            
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()
            
        backtrack(0, 0)

        return res