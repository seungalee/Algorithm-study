import sys

#모든 줄을 한꺼번에 읽어 all에 배열로 받는다
all = sys.stdin.readlines()
all_num = len(all)
dic = {}
for tree in all:
    #개행문자 삭제
    tree_name = tree.rstrip()
    if tree_name not in dic:
        dic[tree_name] = 1
    else:
        dic[tree_name] +=1

#딕셔너리 정렬; 정렬 결과는 배열이므로 dict 통해 다시 딕셔너리로 바꿔준다
dic_sort = dict(sorted(dic.items()))

#round로 하면 0.5 => 0으로 되어 부정확. .f로 처리해야 한다
for key in dic_sort:
    print("%s %.4f" % (key, dic_sort[key]/all_num*100))
    #print(key, round((dic_sort[key]/all_num)*100, 4))
