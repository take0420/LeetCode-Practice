class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = []

        for char in s:
            # 直前の文字と同じなら削除
            if char_stack and char_stack[-1] == char:
                char_stack.pop()
            else:
                char_stack.append(char)

        return "".join(char_stack)
