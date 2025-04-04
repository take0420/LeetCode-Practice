class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}

        for i, num in enumerate(nums):
            if num in hash_table and abs(hash_table[num] - i) <= k:
                return True
            hash_table[num] = i
        
        return False
