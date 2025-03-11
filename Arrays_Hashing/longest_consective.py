class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # 配列内に連続列の開始点が存在するか
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 連続する数をカウント
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # 最大値を更新
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak