from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer: List[List[str]] = []
        check: Dict[str, int] = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in check:
                answer[check[key]].append(word)
            else:
                check[key] = len(answer)
                answer.append([word])

        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
    assert solution.groupAnagrams([""]) == [[""]]
    assert solution.groupAnagrams(["a"]) == [["a"]]
    assert solution.groupAnagrams(["aabb", "abab", "bbaa", "abb"]) == [
        ["aabb", "abab", "bbaa"],
        ["abb"],
    ]
