class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count,ct = 0,0
        len1,len2 = len(nums1),len(nums2)
        i,j = len1-1,len2-1
        lst = []
        midnum = (len1+len2+1)/2
        ans = 0.0
        while count<midnum+1:
            n1,n2 =0,0
            print("sdfa",count)
            if i != -1:
                n1 = nums1[i]
            if j != -1:
                n2 = nums2[j]
            if (n1 >= n2)&(i!=-1):
                lst.append(n1)
                i-=1
            elif (j!=-1) &(n1<n2):
                lst.append(n2)
                j-=1
            else:
                break
            count += 1
            if (count-midnum>-1)&(count-midnum<1):
                ans += lst[count-1]
                ct+=1

        print(lst)
        if ct == 0:
            return 0
        return ans/ct

if __name__ == "__main__":
    num1 = [1,2,3]
    num2 = [4,5,6]

    solu =Solution
    print(solu.findMedianSortedArrays(solu,num1,num2))
