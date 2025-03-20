class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        length = len(nums)

        for i in range(length - 2):
            current_num = nums[i]

            # 最初の数字が正なら、それ以降の合計は必ず正（0より大きい）になるため終了
            if current_num > 0:
                break

            # 同じ数値をスキップ（重複回避）
            if i > 0 and current_num == nums[i - 1]:
                continue

            left, right = i + 1, length - 1

            while left < right:
                total_sum = current_num + nums[left] + nums[right]

                if total_sum == 0:
                    triplets.append([current_num, nums[left], nums[right]])

                    # 重複を避けるため、同じ数値をスキップ
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1

        return triplets
