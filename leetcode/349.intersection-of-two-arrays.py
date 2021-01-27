#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        assume n, m are the length of lists and n < m
        sort the shorter list, O(nlogn)
        iterate longer list to search item in shorter list, O(mlogn)
        check if the value is in intersection list, O(n)
        time complexity : O(nlogn) + O(mlogn) + O(n)
        space complexity: O(nlogn)
        """
        intersectList = []
        if len(nums1) < len(nums2):
            nums1.sort()
            for v in nums2:
                pos = self.binarySearch(nums1, v)
                if pos != -1 and v not in intersectList:
                    intersectList.append(v)
        else:
            nums2.sort()
            for v in nums1:
                pos = self.binarySearch(nums2, v)
                if pos != -1 and v not in intersectList:
                    intersectList.append(v)
        return intersectList


# @lc code=end

