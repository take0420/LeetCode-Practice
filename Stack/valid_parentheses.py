# 1. 辞書を作成し閉じ括弧をキー、対応する開き括弧をバリューとしてマッピングする。
# 2. スタックを用意して開き括弧が現れたらスタックに追加。
# 3. 閉じ括弧が現れたらスタックのトップと比較して対応していれば pop() する。
# 4. 対応していない場合は無効なので False を返す。
# 5. 最後にスタックが空なら True、空でなければ False を返す。

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in bracket_map:  # 閉じ括弧の場合
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:  # 開き括弧の場合
                stack.append(char)

        return not stack