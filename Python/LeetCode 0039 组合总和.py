class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯算法
        ans = []
        def getSum(nums: List[int], beginPlace: int):
            for i in range(beginPlace,len(candidates)):
                sum_num = sum(nums) + candidates[i]
                if sum_num <= target:
                    ab = nums.copy()
                    ab.append(candidates[i])
                    if sum_num == target:
                        ans.append(ab)
                    else:
                        getSum(ab,i)
        getSum([],0)
        return ans