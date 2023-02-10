class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_save = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            save = min(height[left], height[right]) * (right - left)
            if height[left] < height[right] :
                left += 1
            else:
                right -= 1
            max_save = max(max_save, save)
        return max_save