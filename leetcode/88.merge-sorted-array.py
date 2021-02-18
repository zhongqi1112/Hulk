#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        time complexity : O(log(n))
        space complexity: O(n)
        """
        # for i in range(m, m+n):
        #     nums1[i] = nums2[i-m]
        # nums1.sort()
        nums = [0 for i in range(m + n)]

        i = j = k = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            nums[k] = nums1[i]
            i += 1
            k += 1
        
        while j < n:
            nums[k] = nums2[j]
            j += 1
            k += 1
        
        nums1[:(m+n)] = nums[:(m+n)]
        
# @lc code=end

