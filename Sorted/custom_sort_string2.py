class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts = collections.Counter(s)
        result = []

        for char in order:
            if char in s_counts:                    
                result.append(char * s_counts[char])
                del s_counts[char]

        for char, count in s_counts.items():
            result.append(char * count)

        return "".join(result)
