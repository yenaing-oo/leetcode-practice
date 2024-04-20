# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNumCount = 0
        cursorIdx = 0
        lastUniqueNum = -101
        for i in range(0, len(nums)):
            if(nums[i] != lastUniqueNum):
                lastUniqueNum = nums[i]
                nums[cursorIdx] = lastUniqueNum
                uniqueNumCount += 1
                cursorIdx += 1
        return uniqueNumCount