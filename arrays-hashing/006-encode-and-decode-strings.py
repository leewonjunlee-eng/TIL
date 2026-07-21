from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []

        for word in strs:
            parts.append(str(len(word)) + "#" + word)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        answer = []
        index = 0

        while index < len(s):
            hash_index = index

            while s[hash_index] != "#":
                hash_index += 1

            length = int(s[index:hash_index])
            start = hash_index + 1
            end = start + length

            answer.append(s[start:end])
            index = end

        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.decode(solution.encode(["neet", "code", "love", "you"])) == [
        "neet",
        "code",
        "love",
        "you",
    ]
    assert solution.decode(solution.encode(["", "#", "hello#world"])) == [
        "",
        "#",
        "hello#world",
    ]
    assert solution.decode(solution.encode(["abcdefghijkl"])) == ["abcdefghijkl"]
