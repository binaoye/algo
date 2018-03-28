class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        d = {}
        if s == "" or s is None:
            return 0
        for i in range(len(s)):
            if (s[i] in d.keys()):
                if d.get(s[i])>= start:
                    start = d[s[i]] + 1
            d[s[i]] = i
            tmp = i - start + 1
            res = max(res,tmp)
        return res






if __name__ == "__main__":
    solu = Solution
    print(solu.lengthOfLongestSubstring(solu,"dccabccdcca"))