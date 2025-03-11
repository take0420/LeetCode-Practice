class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num: int) -> int:
            # num を mapping に基づいて変換し、その整数値を返す
            mapped_value = 0
            for digit in str(num):
                mapped_value = mapped_value * 10 + mapping[int(digit)]
            return mapped_value
        
        # Python の組み込み sort は安定ソートであり、
        # key が同じ場合は元の順序を維持するため index を別途持たせる必要はない
        sorted_nums = sorted(nums, key=get_mapped_value)
        return sorted_nums
