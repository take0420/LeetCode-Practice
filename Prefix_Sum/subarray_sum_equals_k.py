class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += counter[prefix_sum]
            counter[prefix_sum] = counter[prefix_sum] + 1
        return count
