class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        l, r = -1, n
        l_heap, r_heap = [], []
        total_cost = 0

        while k:
            while len(l_heap) < candidates and l+1 < r:
                l += 1
                heappush(l_heap, costs[l])
            
            while len(r_heap) < candidates and l < r-1:
                r -= 1
                heappush(r_heap, costs[r])
            
            if l_heap and r_heap:
                if l_heap[0] <= r_heap[0]:
                    total_cost += heappop(l_heap)
                else:
                    total_cost += heappop(r_heap)
            elif l_heap:
                total_cost += heappop(l_heap)
            elif r_heap:
                total_cost += heappop(r_heap)
            
            k -= 1
        
        return total_cost
