class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largestは、全体の要素数からk番目に小さい要素に相当するため、
        # k_smallest を len(nums) - k とします。
        k_smallest = len(nums) - k
        
        def partition(left: int, right: int) -> int:
            # ランダムにピボットを選択してリストの最後に移動
            pivot_index = random.randint(left, right)
            pivot_value = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            store_index = left
            # ピボットより小さい要素を左側に移動
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
                    
            # ピボットを最終位置に移動
            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index
        
        def quickSelect(left: int, right: int) -> int:
            # リストに1つの要素しかない場合、その要素を返す
            if left == right:
                return nums[left]
            
            # ピボット位置を取得
            pivot_index = partition(left, right)
            
            if pivot_index == k_smallest:
                return nums[pivot_index]
            elif pivot_index < k_smallest:
                # kth smallest が右側にある場合
                return quickSelect(pivot_index + 1, right)
            else:
                # kth smallest が左側にある場合
                return quickSelect(left, pivot_index - 1)
        
        return quickSelect(0, len(nums) - 1)
