import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for p in string.punctuation:
            s = s.replace(p, '').replace(' ', '').lower()
        n = int(len(s)/2)
        l1 = []
        l2 = []
        for i in range (n):
            l1.append(s[i])
            l2.append(s[-(i+1)])
        if l1 == l2: return True
        return False