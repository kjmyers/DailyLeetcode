class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        minuteAngle = minutes/60 * 360

        hourAngle = hour/12 * 360
        hourAngle += minutes/60 * 30 # 30 is degress in hour

        ret = abs(minuteAngle - hourAngle)
        return min(ret, 360 - ret)
