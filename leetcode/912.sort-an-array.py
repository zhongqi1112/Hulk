#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Bubble Sort
        Time complexity : O(n^2)
        Space complexity: O(1)
        Sorting In Place: Yes
        Stable: Yes
        """
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # return nums

        """
        Selection Sort
        Time complexity : O(n^2)
        Space complexity: O(1)
        Sorting In Place: Yes
        Stable: No
        """
        # for i in range(len(nums)):
        #     min_i = i
        #     for j in range(i+1, len(nums)):
        #         if nums[min_i] > nums[j]:
        #             min_i = j
        #     nums[min_i], nums[i] = nums[i], nums[min_i]
        # return nums

        """
        Intersection Sort
        Time complexity : O(n^2)
        Space complexity: O(1)
        Sorting In Place: Yes
        Stable: Yes
        """
        # for i in range(1, len(nums)):
        #     key = nums[i]
        #     j = i - 1
        #     while j >= 0 and key < nums[j]:
        #         nums[j + 1] = nums[j]
        #         j -= 1
        #     nums[j + 1] = key
        # return nums

        """
        Merge Sort
        Time complexity : O(nlogn)
        Space complexity: O(n)
        Sorting In Place: No
        Stable: Yes
        """
        # if len(nums) > 1:
        #     mid = len(nums) // 2
        #     L = nums[:mid]
        #     R = nums[mid:]

        #     self.sortArray(L)
        #     self.sortArray(R)

        #     i = j = k = 0
        #     while i < len(L) and j < len(R):
        #         if L[i] < R[j]:
        #             nums[k] = L[i]
        #             i += 1
        #         else:
        #             nums[k] = R[j]
        #             j += 1
        #         k += 1
            
        #     while i < len(L):
        #         nums[k] = L[i]
        #         i += 1
        #         k += 1
            
        #     while j < len(R):
        #         nums[k] = R[j]
        #         j += 1
        #         k += 1
        # return nums

        """
        Quick Sort
        Time complexity : O(nlogn)
        Space complexity: O(n)
        Sorting In Place: Yes
        Stable: No
        """
        # self.quickSort(nums, 0, len(nums) - 1)
        # return nums


    def quickSort(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)

            self.quickSort(nums, low, pi - 1)
            self.quickSort(nums, pi + 1, high)

    
    def partition(self, nums, low, high):
        i = low - 1
        pivot = nums[high]

        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i + 1] , nums[high] = nums[high], nums[i + 1]
        return i+1
        
# @lc code=end

