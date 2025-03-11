class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        # 各単語の文字をカウントして、アナグラムのグループ分けを行うため
        for word in strs:
            # インデックス 0-25 を各文字 a-z に対応させるため
            char_count = [0] * 26
            for char in word:
                # ord(char) - ord('a') で a-z を 0-25 のインデックスに変換
                # リストの該当位置を +1 して出現回数を記録
                char_count[ord(char) - ord('a')] += 1
            # char_count を辞書のキーにするためイミュータブルに変換して単語をリストに追加
            groups[tuple(char_count)].append(word)
         # 辞書の値（dict_values）を list に変換して返す
        return list(groups.values())
