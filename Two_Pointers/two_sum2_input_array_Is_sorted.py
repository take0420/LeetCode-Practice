class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed のため +1
            elif current_sum > target:
                right -= 1  # 合計が大きすぎるので右側を狭める
            else:
                left += 1  # 合計が小さすぎるので左側を広げる

        return []  # 必ず解が1つある前提なので、この行は実行されない
