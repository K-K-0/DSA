from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # efficient Approach

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

        # Approach - 1

        # s = sorted(s)
        # t = sorted(t)

        # if s == t:
        #     return True
        # else:
        #     return False

        # s = set(s)
        # t = set(t)

        # Approach - 2

        # if len(s) != len(t):
        #     return False

        # for i in set(s):
        #     if s.count(i) != t.count(i):
        #         return False
        # return True