class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return set(len(nums)) < len(nums)
