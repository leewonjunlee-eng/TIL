class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        count2 = {}
        for char in s1:
            count[char] = count.get(char, 0) + 1
        
        left = 0
        
        for right, char in enumerate(s2):
            if char in count:
                count2[char] = count2.get(char, 0) + 1
                if right - left + 1 > len(s1):
                    left_char = s2[left]
                    count2[left_char] -= 1
                    left += 1
                if right - left + 1 == len(s1):
                    if count == count2:
                        return True
            else:
                left = right + 1
                count2 = {}
        
        return False
