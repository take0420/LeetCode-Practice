class Solution:
    def scoreOfParentheses(self, s:str) -> int:
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += max(2 * score, 1) # '()'は 1, それ以外は 2倍する

        return stack[0]