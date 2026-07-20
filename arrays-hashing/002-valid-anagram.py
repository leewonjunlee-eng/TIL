from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts: Dict[str, int] = {}
        counts_2: Dict[str, int] = {}

        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1

        for char in t:
            if char not in counts_2:
                counts_2[char] = 0
            counts_2[char] += 1

        return counts == counts_2


if __name__ == "__main__":
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") is True
    assert solution.isAnagram("rat", "car") is False
    assert solution.isAnagram("aab", "aba") is True
    assert solution.isAnagram("aab", "abb") is False
