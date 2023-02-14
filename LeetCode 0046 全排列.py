# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         # 递归解决
#         res = []
#         n = len(nums)
#         def getAns(num_s,num_save):
#             if not num_save:
#                 res.append(num_s)
#                 return
#             for i in num_save:
#                 num_new = num_s.copy()
#                 num_new.append(i)
#                 num_save2 = num_save.copy()
#                 num_save2.remove(i) 
#                 getAns(num_new,num_save2)
#         getAns([],nums)
#         return res
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res
