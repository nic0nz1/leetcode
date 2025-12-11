1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        sorted_s = sorted(s)
4        sorted_t = sorted(t)
5        return sorted_s == sorted_t