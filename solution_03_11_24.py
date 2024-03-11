class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a frequency table
        freq = defaultdict(int)

        # Initialize frequencies of letters
        # freq[c] = frequency of char c in s
        for l in s:
            freq[l] += 1
        
        # Iterate order string to append to result
        res = ""
        for l in order:
            while freq[l] > 0:
                freq[l] -= 1
                res += l
        
        # Iterate through freq and append remaining letters
        # This is necessary because some letters may not appear in `order`
        for l,c in freq.items():
            while c > 0:
                c -= 1
                res += l
        
        return res
