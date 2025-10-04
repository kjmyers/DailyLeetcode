class Solution:
    def maxArea(self, height: List[int]) -> int:
        head = 0
        end = len(height) - 1
        
        area = 0
        
        while head != end:
            area = max(area, min(height[head],height[end]) * (end - head))
            if height[head] > height[end]:
                end -= 1
            else:
                head += 1
        
        return area
