class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic_order = collections.defaultdict(int)

        for i in range(len(order)):
            dic_order[order[i]] = i
        return "".join(sorted(s, key=lambda c: dic_order[c]))