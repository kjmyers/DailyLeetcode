class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in range(len(A) - 1))

        ans = 0
        # cur : all rows we have written
        # For example, with str = ["abc","def","ghi"] we might have
        # cur = ["ab", "de", "gh"].
        cur = [""] * len(strs)  

        for col in zip(*strs):
            # cur2 : What we potentially can write, including the
            #        newest column 'col'.
            # Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
            # then cur2 = ["abc","def","ghi"].
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1

        return ans
