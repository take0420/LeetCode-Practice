class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            # ディクショナリでキーが数値、値を出現回数とする
            counter[num] += 1
            # その数値の出現回数が1より大きくなった場合、すなわち重複がある場合はTrueを返す
            if counter[num] > 1:
                return True
        return False