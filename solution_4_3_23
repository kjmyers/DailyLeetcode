class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        front = 0
        back = len(people)-1

        ret = 0

        while front <= back:
            if people[front] + people[back] <= limit:
                back -= 1
            
            ret += 1
            front += 1
        
        return ret
