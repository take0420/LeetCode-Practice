def is_palindrome(s: str) -> bool:
  right, left = 0, len(s) - 1
  while left < right: # pointer が交差するまで
    if s[left] != s[right]:
      return False
    right += 1
    left  -= 1

  return True
