class Solution:
    def simplifyPath(self, path: str) -> str:
        # パスを '/' で区切り、空の部分を除外
        directories = [dir for dir in path.split("/") if dir]
        stack = []

        for dir in directories:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir != ".":
                stack.append(dir)

        # '/' で結合し、ルートを確保
        return "/" + "/".join(stack)
