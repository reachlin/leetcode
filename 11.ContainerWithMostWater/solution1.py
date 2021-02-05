class Solution:
    containers = {}
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maxWater = 0
        self.containers = {}
        for right in range(1,length):
            if right==1:
                water = min(height[0], height[right])*1
                self.containers[1] = water
            else:
                self.containers[right] = self.findMax(right, height)
        #print(self.containers)
        return max(self.containers.values())
    
    def findMax(self, right: int, height: List[int]) -> int:
        leftMax = self.containers[right-1]
        if height[right]==0:
            return leftMax
        maxWidth = int(leftMax/height[right])
        if leftMax%height[right]>0:
            maxWidth += 1
        if maxWidth > right:
            return leftMax
        elif maxWidth == right:
            return max(leftMax, min(height[0],height[right])*maxWidth)
        else:
            maxWater = leftMax
            for left in range(right):
                water = min(height[left],height[right])*(right-left)
                maxWater = max(maxWater, water)
            return maxWater
        