class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ALPHABET_SIZE = 26
        # 最初の単語の文字出現回数を記録する配列
        count = [0] * ALPHABET_SIZE

        # 最初の単語の各文字をカウントする
        for char in words[0]:
            count[ord(char) - ord('a')] += 1
        
        #  # 残りの単語で、各文字の共通の最小出現回数を更新する
        for word in words[1:]:
            cur_cnt = [0] * ALPHABET_SIZE
            for char in word:
                cur_cnt[ord(char) - ord('a')] += 1
            for i in range(ALPHABET_SIZE):
                count[i] = min(count[i], cur_cnt[i])

        # 全単語で共通する各文字を出現回数分だけリストに追加
        res = []
        for i in range(ALPHABET_SIZE):
            res.extend([chr(i + ord('a'))] * count[i])
        return res

