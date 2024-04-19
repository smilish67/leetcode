# my fisrt attempt was filing nums1's empty areas with nums2. and sorting using selection sort
# time-complexity : O(n^2)
# Another method could be different sorting algorithms like merge. (O(n*logN))

# This problem asks conquer process since it gives already sorted two divided arrays.

# So my second attempt was Two pointer algo to solve conquer process sequentially.
# important point is that i have to satisfy below conditions
# 1. Using two pointer but chainging nums1 arr
# 2. Comparing from 0 index is unefficient, since it has pushing other list variables (or we can use linked list but the example's isn't, so leave aside.)

# But nums1's last n index are meaningless therefore we can use these without pushing.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # only merge step.
        i = m-1
        j = n-1
        k = m+n-1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            
