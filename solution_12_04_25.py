class Solution:
    def countCollisions(self, directions: str) -> int:
        st = False
        rc = 0
        ret = 0

        for d in directions:
            if  d == 'R':
                rc += 1
                st = False
            elif d == 'S':
                ret += rc
                rc = 0
                st = True
            elif d == 'L':
                if st:
                    ret += 1
                    # st still True
                elif rc > 0:
                    ret += rc + 1
                    rc = 0
                    st = True
        
        return ret
