class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        d1 = {}
        d2 = {}
        if len(indexes) == 0:
            return S
        if len(indexes) == 1:
            return S[:indexes[0]] + S[indexes[0]:].replace(sources[0], targets[0])
        ans = ""
        for j in range(len(indexes)):
            d1[indexes[j]] = sources[j]
            d2[indexes[j]] = targets[j]
        indexes.sort()
        print(indexes)
        for i in range(len(indexes) - 1):
            ans = ans + S[indexes[i]:indexes[i + 1]].replace(d1[indexes[i]], d2[indexes[i]])
        ans = ans + S[indexes[len(indexes) - 1]:].replace(d1[indexes[len(indexes) - 1]], d2[indexes[len(indexes) - 1]])
        print(ans)
        if indexes[0] > 0:
            ans = S[0:indexes[0]] + ans
        return ans


    def rev(lst):
        ans = []
        for x in lst:
            if x == 1:
                ans.append(0)
            else:
                ans.append(1)
        return ans



if __name__ == "__main__":
    s = "abcd"
    indexes = [0, 2]
    sources = ["ab", "ec"]
    targets = ["eee", "ffff"]
    solu = Solution
    print(solu.findReplaceString(solu,s,indexes,sources,targets))
