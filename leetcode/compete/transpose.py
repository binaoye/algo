class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        l, m = len(A[0]), len(A)
        if m == 0:
            return []
        ans = [[0 for i in range(m)] for j in range(l)]
        print(ans)
        for i in range(l):
            for j in range(m):
                print(i, j, A[j][i], ans[i], ans[i][j])
                ans[i][j] = A[j][i]
        print(ans)
        return ans

if __name__ == "__main__":
    solu = Solution
    a = [[1,2,3],[4,5,6],[7,8,9]]
    print(solu.transpose(solu, a))