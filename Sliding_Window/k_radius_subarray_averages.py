class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return nums  # ウィンドウサイズ1なら処理不要なため
        
        window_size = 2 * k + 1  # 中心から左右にkずつ全体で必要な要素数
        averages = [-1] * n  # ウィンドウが形成できない場所は-1にするため
        
        if window_size > n:
            return averages
        
        current_window_sum = sum(nums[:window_size])  # 初期ウィンドウの和を一度に計算して無駄な計算を避けるため
        averages[k] = current_window_sum // window_size  # ウィンドウの平均を設定するため
        
        for center in range(k + 1, n - k):
            current_window_sum += nums[center + k] - nums[center - k - 1]  # ウィンドウ移動時に和を更新するため
            averages[center] = current_window_sum // window_size  # 更新後の平均を記録するため
        
        return averages
