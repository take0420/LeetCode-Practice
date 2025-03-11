class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        right_sum = sum(nums)  # 右側の全体の合計
        left_sum = 0  # 左側の累積和

        for i, num in enumerate(nums):
            right_sum -= num  # 右側の合計から現在の要素を引く
            left_contribution = i * num - left_sum  # 左側の絶対値差の合計
            right_contribution = right_sum - (n - i - 1) * num  # 右側の絶対値差の合計
            result[i] = left_contribution + right_contribution
            left_sum += num  # 左側の累積和を更新

        return result
