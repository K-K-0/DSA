class Solution:
    def frequencySort(self, s: str) -> str:

        dic = {}
        r = []


        for i in s:
            dic[i] = dic.get(i, 0) + 1
        sort = sorted(dic.items(), key=lambda x:-x[1])

        for i, j in sort:
            r += [i] * j
        return ''.join(r)      