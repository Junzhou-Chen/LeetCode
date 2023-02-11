class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心算法
        maxPos, end, step = 0, 0, 0
        # maxPos：最远跳跃距离，end:最远右边界，step：跳跃次数
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, i + nums[i])
            # 更新最远跳跃距离
            if i == end:
                # 到达边界，开始跳跃
                end = maxPos
                step += 1
        return step