class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        a = self.rfv(self,A)
        b = self.rfv(self,B)
        ast = self.flatmap(self, a)
        bst = self.flatmap(self, b)
        count = 0
        for i in range(len(ast)):
            if ast[i] == bst[i] and ast[i] == 1:
                count = count + 1
        return count




    def rev(self, a):
        ans = []
        for s in a:
            if s == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans

    def rfv(self, a):
        ans = []
        for lst in a:
            lst.reverse()
            ans.append(self.rev(self,lst))
        return ans
    def flatmap(self, a):
        ans = []
        for t in a:
            for s in t:
                ans.append(s)
        return ans

if __name__ == "__main__":
    # A = [[1, 1, 0],
    #      [0, 1, 0],
    #      [0, 1, 0]]
    # B = [[0, 0, 0],
    #      [0, 1, 1],
    #      [0, 0, 1]]
    A = [[1]]
    B = [[0]]
    solu = Solution
    # print(solu.rfv(solu, A))
    # print(solu.rfv(solu, B))
    # print(solu.largestOverlap(solu, A, B))