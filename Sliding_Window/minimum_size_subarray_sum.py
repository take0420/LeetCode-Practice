class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0                # ウィンドウの左端
        current_sum = 0         # 現在のウィンドウ内の合計値
        min_length = float("inf")  # 最小の部分配列長を記録
        
        # 右側のポインタでウィンドウを拡大
        for right, num in enumerate(nums):
            current_sum += num
            
            # 現在の合計が target 以上なら、左側からウィンドウを縮小して最小長を更新
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        # もし min_length が更新されていなければ、条件を満たす部分配列は存在しないので 0 を返す
        return 0 if min_length == float("inf") else min_length
