class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT

'''
s = 'anagram'
t = 'nagaram'

i = 0, s = 'a', t ='n' 
    s = {a:1}, t = {n:1}
i = 1, s = 'n', t ='a'
    s = {a:1, n:1}, t = {n:1, a:1} 
i = 2, s = 'a', t ='g' 
    s = {a:2, n:1}, t = {n:1, a:1, g:1} 

etc...

最終的には下記のようになる。
countS = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
countT = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

双方のキーとバリューのペアが同じのため、アナグラムといえる。
'''
