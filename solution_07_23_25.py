class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s: str, pair: str, points: int, stack: list) -> tuple[int, str]:
            score = 0
            for char in s:
                if stack and stack[-1] + char == pair:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return score, ''.join(stack)
        
        # Initialize result and stack
        total_score = 0
        stack = []
        
        # If x >= y, remove "ab" first, then "ba"
        if x >= y:
            # First pass: remove "ab" pairs
            score1, new_s = remove_pair(s, "ab", x, stack)
            stack = []  # Reset stack
            # Second pass: remove "ba" pairs from remaining string
            score2, _ = remove_pair(new_s, "ba", y, stack)
            total_score = score1 + score2
        else:
            # First pass: remove "ba" pairs
            score1, new_s = remove_pair(s, "ba", y, stack)
            stack = []  # Reset stack
            # Second pass: remove "ab" pairs from remaining string
            score2, _ = remove_pair(new_s, "ab", x, stack)
            total_score = score1 + score2
            
        return total_score
