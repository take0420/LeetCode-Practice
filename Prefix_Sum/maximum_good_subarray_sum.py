class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # 累積和を事前計算
        cumulative_sum = [0] * (n + 1)
        for i in range(n):
            cumulative_sum[i + 1] = cumulative_sum[i] + nums[i]

        max_good_sum = float('-inf')  # 最大のGood Subarrayの和
        last_seen_index = {}  # {数値: その数値が最後に出たインデックス}

        for i, num in enumerate(nums):
            # 差の絶対値がkになる数値が過去に出たかチェック
            for target_val in (num - k, num + k):
                if target_val in last_seen_index:
                    j = last_seen_index[target_val]
                    max_good_sum = max(max_good_sum, cumulative_sum[i + 1] - cumulative_sum[j])

            # より大きい部分和を保持するための更新処理
            if num in last_seen_index:
                if cumulative_sum[i + 1] - cumulative_sum[last_seen_index[num]] < nums[i]:
                    last_seen_index[num] = i
            else:
                last_seen_index[num] = i

        return max_good_sum if max_good_sum != float('-inf') else 0
