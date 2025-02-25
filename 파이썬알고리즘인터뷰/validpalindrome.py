class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = []
        for char in s:
            if char.isalpha():
                lower_char = char.lower()
                only_letters.append(lower_char)
            if char.isdigit():
                only_letters.append(char)
        if len(only_letters) == 0:
            return True
        for i in range(len(only_letters)//2 +1):
            if only_letters[i] != only_letters[-(i+1)]:
                return False
        return True

    