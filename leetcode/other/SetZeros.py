class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        mins = max(matrix[0])
        print(mins)
        for i in range(len(matrix)):
            if max(matrix[i]) > mins:
                mins = max(matrix[i])
        mins += 1
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if row[j] == 0:
                    for k in range(len(row)):
                        if k != j and matrix[i][k] != 0:
                            matrix[i][k] = mins
                    for s in range(len(matrix)):
                        if s != i and matrix[s][j] != 0:
                            matrix[s][j] = mins
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == mins:
                    matrix[i][j] = 0



        return matrix






if __name__ == "__main__":
    inp = [
        [0,5,6,6,9],
        [7,0,3,3,1],
        [1,-2147483648,7,2147483647,8]]
    solu = Solution
    ans = solu.setZeroes(solu, inp)
    print(ans)