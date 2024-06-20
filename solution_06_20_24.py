class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def attemptForce(force):
            ret = 0
            distBet = 0
            remBalls = m - 1
            for i in range(1,len(position)):
                distBet += position[i] - position[i-1]
                if distBet >= force:
                    remBalls -= 1
                    distBet = 0
            if remBalls > 0:
                return False
            else:
                return True


        l = 1
        r = int(position[-1] / (m - 1.0)) + 1
        ans = 0
        while l <= r:
            mid = l + (r - l)//2
            if attemptForce(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
