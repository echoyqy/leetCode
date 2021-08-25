from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st) 
        return list(mp.values())

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    sol.groupAnagrams(strs)
