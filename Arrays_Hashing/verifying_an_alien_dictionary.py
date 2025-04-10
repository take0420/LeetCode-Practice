class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = [0] * len(order)
        
        for i in range(len(order)):
            order_dict[ord(order[i]) - ord('a')] = i
            
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            min_len = min(len(w1), len(w2))
            
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return False
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if order_dict[ord(w1[j]) - ord('a')] > order_dict[ord(w2[j]) - ord('a')]:
                        return False
                    break
            
        return True
