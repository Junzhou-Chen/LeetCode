class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if not stack or stack[-1] == i:
                stack.append(i)
            else:
                stack.pop()
        if not stack:
            return -1
        mostnum = stack[-1]
        num = 0
        for i in nums:
            if i == mostnum:
                num += 1
        if num > len(nums) / 2:
            return mostnum
        else:
            return -1
