class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # two steps:first,find target number;senond,find the target number beginning and ending
        # first step:
        left, right = 0, len(nums) - 1
        res = -1
        while(left <= right):
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if res == -1:
            return [-1,-1]
        left = right = res
        n = len(nums) - 1
        while left and nums[left - 1] == target:
                left = left - 1
        while right != n and nums[right + 1] == target:
                right += 1
            
        return [left,right]