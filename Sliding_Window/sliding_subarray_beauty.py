class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # 現在のウィンドウ内の数字の出現頻度を保持するカウンター
        window_counter = collections.defaultdict(int)
        
        # 現在のウィンドウから x 番目に小さい負の整数を探すヘルパー関数
        def find_xth_smallest_negative(x: int) -> int:
            count = 0
            # 負の整数は -50 から -1 の間だけなので、固定範囲でループ
            for num in range(-50, 0):
                count += window_counter[num]
                # もしこれまでのカウントが x 以上になったら、その数字が x 番目の負の整数
                if count >= x:
                    return num
            # x 個の負の整数がない場合は 0 を返す
            return 0
        
        beauty_values = []
        n = len(nums)
        
        # 初期ウィンドウのセットアップ
        for i in range(k):
            window_counter[nums[i]] += 1
        beauty_values.append(find_xth_smallest_negative(x))
        
        # ウィンドウをスライドしながら更新
        for i in range(k, n):
            # ウィンドウの左端の数字をウィンドウから外す
            window_counter[nums[i - k]] -= 1
            # 新しくウィンドウに入る右端の数字を追加する
            window_counter[nums[i]] += 1
            beauty_values.append(find_xth_smallest_negative(x))
        
        return beauty_values
