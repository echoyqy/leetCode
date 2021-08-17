from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_count = Counter(s)
            t_count = Counter(t)
            for key, value in s_count.items():
                if t_count.get(key, 0) != value:
                    return False
            return True

