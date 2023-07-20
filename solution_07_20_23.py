class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        s = []

        for a in asteroids:
            flag = True
            while s and s[-1] > 0 and a < 0:
                if abs(s[-1]) < abs(a):
                    s.pop()
                    continue
                
                elif abs(s[-1] == abs(a)):
                    s.pop()
                
                flag = False
                break
            
            if flag:
                s.append(a)
        
        return s
            
