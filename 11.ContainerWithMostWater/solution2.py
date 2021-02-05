class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maxWater = 0
        left = 0
        right = length -1
        while right>left:
            maxWater = max(maxWater, min(height[left],height[right])*(right-left))
            if height[right]>height[left]:
                left += 1
            else:
                right -= 1
        return maxWater
