class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s = []
        for num in arr:
            if not s or num > s[-1]:
                s.append(num)
            else:
                max_element = s[-1]
                while s and num < s[-1]:
                    s.pop()
                s.append(max_element)
        return len(s)
