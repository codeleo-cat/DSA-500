class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')  # 쪼개고
        s[:] = [el for el in s if el!=''] # 공백 제거
        len_last_word = len(s[-1])
        return len_last_word