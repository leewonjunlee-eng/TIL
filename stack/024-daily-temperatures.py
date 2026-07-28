class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tem = []

        answer = [0] * len(temperatures)
        for index, temper in enumerate(temperatures):
            while tem and tem[-1][0] < temper:
                prev_tem, prev_index = tem.pop()
                answer[prev_index] = index - prev_index

            tem.append((temper, index))

        return answer
