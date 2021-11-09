from collections import defaultdict


class Solution:

    def lemonadeChange(self, bills):
        dic = defaultdict(int)
        for i in bills:
            dic[i] += 1
            diff = i - 5
            while diff:
                if diff >= 10 and dic[10]:
                    dic[10] -= 1
                    diff -= 10
                elif diff >= 5 and dic[5]:
                    diff[5] -= 1
                    diff -= 5
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    bills = [5, 5, 5, 10, 20]
    print(s.lemonadeChange(bills))
