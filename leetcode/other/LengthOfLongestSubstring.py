class Solution(object):
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
            print("start", start)
            if s[i] in d.keys():
                if d.get(s[i]) >= start:
                    start = d[s[i]] + 1
            d[s[i]] = i
            tmp = i - start + 1
            res = max(res, tmp)
        return res




if __name__ == "__main__":
    st = "pwwkew"
    # st= "ab"
    # print(st[1:])
    # print(st[:1])
    solu = Solution
    ans = solu.lengthOfLongestSubstring(solu, st)
    print(ans)
