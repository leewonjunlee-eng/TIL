class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1

        left = 0
        answer_count = 0
        count2 = {}
        low = 10000
        answer = ""

        for right, char in enumerate(s):
            if char in count:
                count2[char] = count2.get(char, 0) + 1

                # 필요한 개수까지만 answer_count에 포함
                if count2[char] <= count[char]:
                    answer_count += 1

            # t의 모든 문자를 포함한 경우
            while answer_count == len(t):
                if right - left + 1 < low:
                    low = right - left + 1
                    answer = s[left:right + 1]

                left_char = s[left]

                if left_char in count:
                    # 왼쪽 문자를 제거
                    count2[left_char] -= 1

                    # 필요한 문자 개수가 부족해진 경우
                    if count2[left_char] < count[left_char]:
                        answer_count -= 1

                left += 1

        return answer
