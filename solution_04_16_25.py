class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        same = 0
        right = 0
        cnt = Counter()
        ans = 0
        for left in range(n):
            while same < k and right < n:
                same += cnt[nums[right]]
                cnt[nums[right]] += 1
                right += 1
            if same >= k:
                ans += n - right + 1
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]
        return ans
