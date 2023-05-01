class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        s = sum(salary[1:(n-1)])
        return s/(n-2)
