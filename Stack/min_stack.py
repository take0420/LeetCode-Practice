class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # スタックに値を追加する。最小値ならば minStack に保存する。
        self.mainStack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        # スタックのトップを削除する。minStack も同時に更新する。
        if self.mainStack:
            self.mainStack.pop()
            self.minStack.pop()

    def top(self) -> int:
        # スタックのトップの値を取得する。
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
