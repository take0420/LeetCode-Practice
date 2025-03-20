jclass Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 配列をソートしておく（重複を防ぐため）
        triplets = []

        for i in range(len(nums) - 2):
            # 同じ数字が続く場合はスキップ（重複回避）
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # 合計が0なら組み合わせを記録
                    triplets.append([nums[i], nums[left], nums[right]])

                    # 重複する組み合わせをスキップ
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 次の候補にポインタを進める
                    left += 1
                    right -= 1

                elif current_sum < 0:
                    left += 1  # 合計が小さいので左ポインタを進める
                else:
                    right -= 1  # 合計が大きいので右ポインタを戻す

        return triplets
