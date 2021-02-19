#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = 0
        for n in arr2:
            # find the first element to swap
            for i in range(pos, len(arr1)):
                if arr1[i] != n:
                    pos = i
                    break
            # find the element matches with arr2
            for i in range(pos+1, len(arr1)):
                if arr1[i] == n:
                    arr1[pos], arr1[i] = arr1[i], arr1[pos]
                    pos += 1
        # bubble sort elements do not appear in arr2 in ascending order
        for i in range(pos, len(arr1)):
            for j in range(pos, len(arr1) - 1):
                if arr1[j] > arr1[j + 1]:
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

        return arr1

# @lc code=end

