def solution(n, words):
    answer = []
    first_word = words.pop(0)
    last_letter = first_word[len(first_word)-1]
    used_word = []
    used_word.append(first_word)
    num=1
    for word in words:
        if word[0]!=last_letter:
            break
        if word in used_word:
            break
        num+=1
        last_letter = word[len(word)-1]
        used_word.append(word)
    if len(used_word) == len(words)+1:
        answer.append(0)
        answer.append(0)
    else:
        if (num+1)%n==0:
            answer.append(n)
        else:
            answer.append((num+1)%n)
        answer.append(num//n +1)
    

    return answer