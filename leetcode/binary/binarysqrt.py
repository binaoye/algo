class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left = 0
        right = x
        mid = 0
        while 1:
            mid = int((left + right) / 2)
            print(mid)
            sqr = mid * mid
            ssr = (mid + 1) * (mid + 1)
            # sfr = (mid - 1) * (mid - 1)
            if sqr <= x:
                if ssr > x:
                    break
                else:
                    left = mid
            else:
                right = mid
        return mid



if __name__ == "__main__":
    solu = Solution
    print(solu.mySqrt(solu, 0))