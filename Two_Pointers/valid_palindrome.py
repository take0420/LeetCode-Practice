class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
          # left pointer を英数字に到達するまで動かす（記号はスキップする）
          while left < right and not s[left].isalnum():
            left += 1
          # right pointer を英数字に到達するまで動かす（記号はスキップする）
          while left < right and not s[right].isalnum():
            right -= 1

          # 英数字を小文字にする処理
          if s[left].lower() != s[right].lower():
            return False

          left += 1
          right -= 1

        return True
