class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)  # 各果物の数を保持
        left = 0                        # ウィンドウの左端
        max_fruits = 0                  # 最大収穫数の記録

        for right in range(len(fruits)):
            fruit = fruits[right]
            fruit_count[fruit] += 1

            # バスケットに3種類以上ある場合、左端から果物を減らす
            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
                left += 1

            # 現在のウィンドウサイズで最大値を更新
            current_window_size = right - left + 1
            max_fruits = max(max_fruits, current_window_size)

        return max_fruits
