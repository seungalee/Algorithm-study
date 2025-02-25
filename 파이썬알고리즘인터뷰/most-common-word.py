class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.split(r"[ ,]", paragraph)
        print(words)
        dic = {}
        for word in words:
            filtered_word = word.lower()
            filtered_word = re.sub('[^a-z]', '', filtered_word)
            if filtered_word:
                if filtered_word not in banned:
                    if filtered_word in dic:
                        dic[filtered_word]+=1
                    else:
                        dic[filtered_word] = 1
        sorted = collections.Counter(dic)
        key, value = sorted.most_common(1)[0]
        return key