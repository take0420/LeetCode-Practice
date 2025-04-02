class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > 1:
                return True
        return False
