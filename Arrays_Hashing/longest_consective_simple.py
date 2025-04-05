class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums) # 重複の値は排除した集合
    longest = 0
    
    for num in numSet:
      # num が連続する値の視点である場合のみカウントを開始する
      if num - 1 not in numSet:
        len = 1
        while num + len in numSet:
          len += 1
        longest = max(longest, len)
    
    return longest
