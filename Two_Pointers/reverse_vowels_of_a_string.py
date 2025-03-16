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
