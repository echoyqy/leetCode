def isAnagram(s: str, t: str):
    l_l = list(s)
    l_l.sort()
    s_l = "".join(l_l)
    l_r = list(t)
    l_r.sort()
    s_r = "".join(l_r)
    return s_l == s_r


# plan2
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)
        for key, value in s_count.items():
            t_value = t_count.get(key, 0)
            if value != t_value:
                return False
        return True