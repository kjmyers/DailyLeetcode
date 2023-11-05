class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        
        count = 0
        while count != k:
            if arr[0] > arr[1]:
                count += 1
                arr.append(arr[1])
                del arr[1]
            else:
                count = 1
                arr.append(arr[0])
                del arr[0]
        return arr[0]
            
