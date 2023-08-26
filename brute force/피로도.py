def goDungeon(k, dungeons, answer, answers):
    for dungeon in dungeons:
        nowdungeons = dungeons.copy()
        nowk = k
        if nowk>=dungeon[0]:
            nowk-=dungeon[1]
            answer+=1
            nowdungeons.remove(dungeon)     
        else: 
            nowdungeons.remove(dungeon)
        if nowdungeons==[]:
                answers.append(answer)
        goDungeon(nowk, nowdungeons, answer, answers)

def solution(k, dungeons):
    answers = []
    goDungeon(k, dungeons, 0, answers)
    answer = max(answers)
    return answer

solution(80, [[80,20],[50,40],[30,10]])