class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        right_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum -= num
            left_total = i * num - left_sum # 左側の絶対値差の合計
            right_total = right_sum - (n-i-1) * num # 右側の絶対値差の合計
            res[i] = right_total + left_total
            left_sum += num # 左側の累積和を更新する

        return res
