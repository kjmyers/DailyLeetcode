class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        seen1 = defaultdict(int)
        seen2 = defaultdict(int)

        s1 = [node1]
        s2 = [node2]
        d1 = -1
        d2 = -1

        while s1 or s2:
            if s1:
                cur1 = s1.pop()
                d1 += 1
                if cur1 not in seen1.keys():
                    seen1[cur1] = d1
                    if edges[cur1] != -1:
                        s1.append(edges[cur1])
            if s2:
                cur2 = s2.pop()
                d2 += 1
                if cur2 not in seen2.keys():
                    seen2[cur2] = d2
                    if edges[cur2] != -1:
                        s2.append(edges[cur2])
            
            #print(cur1,cur2)
            if cur1 in seen2.keys() and cur2 in seen1.keys():
                totD1 = d1 + seen2[cur1]
                totD2 = d2 + seen1[cur2]
                print(totD1,totD2)
                if totD1 == totD2:
                    return min(cur1,cur2)
                elif totD1 < totD2:
                    return cur2
                else:
                    return cur1
            elif cur1 in seen2.keys():
                return cur1
            elif cur2 in seen1.keys():
                return cur2

        
        return -1



        
