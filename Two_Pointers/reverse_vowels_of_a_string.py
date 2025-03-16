# Base

def reverse_string(s: List[str]):
    # 先頭と末尾を指す二つのポインタを初期化
    left, right = 0, len(s) - 1

    # leftとrightが重なるまでループ
    while left < right:
        # スワップ操作
        s[left], s[right] = s[right], s[left]
        # ポインタを移動
        left, right = left + 1, right - 1

    return s


# Solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # 母音のセット（大文字小文字両対応）
        s_list = list(s)  # 文字列は変更不可なのでリスト化
        left, right = 0, len(s) - 1

        while left < right:
            # 左ポインタを母音が出るまで右へ進める
            while left < right and s_list[left] not in vowels:
                left += 1

            # 右ポインタを母音が出るまで左へ進める
            while left < right and s_list[right] not in vowels:
                right -= 1

            # 左右の母音を入れ替える
            s_list[left], s_list[right] = s_list[right], s_list[left]

            # 入れ替え後、次の文字へ進める
            left += 1
            right -= 1

        return "".join(s_list)

# 計算量
# - Time complexity: O(N)  # 文字列を一度だけ走査
# - Space complexity: O(N) # リストに変換した文字列を保持
