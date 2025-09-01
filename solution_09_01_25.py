class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Lambda to calculate the gain of adding an extra student
        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students
        
        ratios = []
        for x,y in classes:
            gain = _calculate_gain(x,y)
            heappush(ratios, (-gain, x, y))
        
        totalClasses = len(ratios)
        ret = 0.0
        for s in range(extraStudents):
            curg, passes, total = heappop(ratios)
            heappush(ratios, (-_calculate_gain(passes+1,total+1),passes+1,total+1))
        
        for _,passes,total in ratios:
            ret += passes/total


        return ret/totalClasses
