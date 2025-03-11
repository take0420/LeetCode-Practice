class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strs = list(map(str, nums))
        
        def compare_nums(first: str, second: str) -> int:
            if first + second > second + first:
                return -1
            elif first + second < second + first:
                return 1
            return 0
        
        num_strs.sort(key=cmp_to_key(compare_nums))
        return "0" if num_strs[0] == "0" else "".join(num_strs)
