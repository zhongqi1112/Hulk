#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        A = self.M.get(key)
        if A is None:
            return ""
        # chr(127) #--> '\x7f' memory address of [DEL] in hex
        i = bisect.bisect(A, (timestamp, chr(127)))
        if i > 0:
            return A[i-1][1]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

