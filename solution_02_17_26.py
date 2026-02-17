class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for i in range(1024):
            h, m = (
                i >> 6, # Drop first 6
                i & 0x3F, # mask all but first 6: 0011 1111
            )  # Extract the high 4 bits and low 6 bits using bitwise operations
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans
