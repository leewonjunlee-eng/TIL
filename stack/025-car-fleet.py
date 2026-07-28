class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        for pos, speed in cars:
            if stack and stack[-1] >= (target - pos) / speed:
                continue
            else:
                stack.append((target - pos) / speed)

        return len(stack)
