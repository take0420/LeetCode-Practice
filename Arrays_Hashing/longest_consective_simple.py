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

'''
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
-----------------
初期状態
- nums = [100, 4, 200, 1, 3, 2]
- numSet = {1, 2, 3, 4, 100, 200}
- longest = 0

反復処理
【num = 1】
- 条件: 1 - 1 = 0 が numSet にない → 1 は連続シーケンスの始点
`- while ループ: 1 + 1 = 2 が numSet にある → length = 2
`- length を 1 に初期化
`: 1 + 2 = 3 が numSet にある → length = 3
`: 1 + 3 = 4 が numSet にある → length = 4
: 1 + 4 = 5 が numSet にないのでループ終了
`- longest を max(0, 4) = 4 に更新

【num = 2】
`- 条件: 2 - 1 = 1 が numSet にある → 2 は連続シーケンスの途中なのでスキップ

【num = 3】
`- 条件: 3 - 1 = 2 が numSet にある → スキップ

【num = 4】
`- 条件: 4 - 1 = 3 が numSet にある → スキップ

【num = 100】
`- 条件: 100 - 1 = 99 が numSet にない → 100 は始点
`- length を 1 に初期化
`- while ループ: 100 + 1 = 101 が numSet にないのでループ終了
`- longest を max(4, 1) = 4 に更新（変化なし）

【num = 200】
`- 条件: 200 - 1 = 199 が numSet にない → 200 は始点
`- length を 1 に初期化
`- while ループ: 200 + 1 = 201 が numSet にないのでループ終了
`- longest を max(4, 1) = 4 に更新

ループ終了後、longest の値は 4 となり、最終的に 4 が返される
'''
