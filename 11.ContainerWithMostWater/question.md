## 11. Container With Most Water
Medium

8272

656

Add to List

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

## solution1
Time Limit Exceeded

## solution2
Success
Details 
Runtime: 368 ms, faster than 5.19% of Python3 online submissions for Container With Most Water.
Memory Usage: 16.8 MB, less than 20.90% of Python3 online submissions for Container With Most Water.
Next challenges:
Trapping Rain Water

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104
Accepted
837,674
Submissions
1,600,703