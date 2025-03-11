class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 各文字をエイリアン言語での順位（インデックス）に変換する辞書を作成
        char_order = {char: idx for idx, char in enumerate(order)}

        # 隣り合う単語同士を比較する
        for word1, word2 in zip(words, words[1:]):
            # 2つの単語のうち、短い方の長さまで文字を比較
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    # 異なる文字が見つかった場合、エイリアン言語の順序をもとに大小を判断
                    if char_order[word1[i]] > char_order[word2[i]]:
                        return False
                    # ここで比較が終了するので、内側のループを抜ける
                    break
            else:
                # 全ての文字が同じだった場合、
                # 長い単語が先に来るのは正しくないので、その場合はFalseを返す
                if len(word1) > len(word2):
                    return False
        return True
