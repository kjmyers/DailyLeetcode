class Solution:
    def minLength(self, s: str) -> int:
        st = []
        n = len(s)

        for i in range(n):
            if st and ((s[i] == "B" and st[-1] == "A") or (s[i] == "D" and st[-1] == "C")):
                st.pop()
            else:
                st.append(s[i])
        
        return len(st)
