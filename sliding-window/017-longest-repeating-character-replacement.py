class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_count = 0
        best = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            max_count = max(max_count, count[char])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
