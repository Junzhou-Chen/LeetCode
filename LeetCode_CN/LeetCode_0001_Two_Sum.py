class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            _target = target - nums[i]
            if _target in numMap:
                return [numMap[_target], i]
            else:
                numMap[nums[i]] = i
                
        return []
