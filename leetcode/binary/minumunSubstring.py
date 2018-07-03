class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def to_dic(s):
            dic_s = {}
            for i in s:
                if i in dic_s.keys():
                    dic_s[i] += 1
                else:
                    dic_s[i] = 1
            return dic_s

        ns, nt = len(s), len(t)
        if nt > ns:
            return ""
        dic_t = to_dic(t)
        sz = dic_t.keys()
        anslen = ns + 1
        ans_left = 0
        ans_right = -1
        print(dic_t)
        for i in range(ns):
            count = 0
            newdic = {}
            left = i
            right = -1
            for j in range(i, ns):
                if count < len(sz):
                    if s[j] in sz:
                        if s[j] not in newdic.keys():
                            print('add', j)
                            newdic[s[j]] = 1
                            count += 1
                        else:
                            if newdic[s[j]] < dic_t[s[j]]:
                                print('add')
                                count += 1
                                newdic[s[j]] += 1
            print(count, nt)
            if count == nt:
                print('right', j + 1, 'left', left)
                right = j + 1
                break
            if right >= 0:
                if right - left < anslen:
                    ans_left = left
                    ans_right = right
                    print('dfas', ans_left, 'fds', ans_right)
                    anslen = right - left
        print('left', ans_left, 'right', ans_right)
        return s[ans_left:ans_right + 1]




if __name__ == "__main__":
    solu = Solution
    print(solu.minWindow(solu, "AA", "AA"))



