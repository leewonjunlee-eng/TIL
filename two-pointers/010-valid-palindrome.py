class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = []
        backward = []
        filtered = "".join(char.lower() for char in s if char.isalnum())

        for char in filtered:
            forward.append(char)

        for char in reversed(filtered):
            backward.append(char)

        return forward == backward


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True
