class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        log_letters = []
        log_digits = []
        for log in logs:
            if log.split()[1].isalpha():
                log_letters.append(log)
            else:
                log_digits.append(log)
        log_letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return log_letters+log_digits