class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for letter in s:
            if letter not in table:
                stack.append(letter)
            elif not stack or table[letter]!=stack.pop():
                return False
        
        return len(stack)==0

        