class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 最初のウィンドウの合計を計算
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # ウィンドウを1つずつ右にずらしながら最大合計を探す
        for i in range(k, len(nums)):
            # 左端の要素を引き、右端の要素を足す
            window_sum += nums[i] - nums[i - k]
            # 最大合計を更新する
            max_sum = max(max_sum, window_sum)
        
        # 最大合計をkで割ると最大平均値が求められる
        return max_sum / k
