def solution(today, terms, privacies):
    answer = []
    today_arr = [0]*3
    today_arr[0], today_arr[1], today_arr[2] = map(int, today.split("."))
    dic = {}
    count =1
    for term in terms:
        now = term.split()
        dic[now[0]] = now[1]
    for privacy in privacies:
        privacy_arr = privacy.split()
        privacy_date = privacy_arr[0]
        privacy_alp = privacy_arr[1]
        privacy_date_arr = [0]*3
        privacy_date_arr[0], privacy_date_arr[1], privacy_date_arr[2] = map(int, privacy_date.split("."))
        privacy_date_arr[1] += int(dic[privacy_alp])
        if privacy_date_arr[2]==1:
            privacy_date_arr[1]-=1
            privacy_date_arr[2]=28
        else:
            privacy_date_arr[2]-=1
        privacy_date_arr[0] = privacy_date_arr[0] + privacy_date_arr[1]//12
        privacy_date_arr[1] = privacy_date_arr[1]%12
        if(privacy_date_arr[1]==0):
            privacy_date_arr[1] = 12
            privacy_date_arr[0] -= 1
                
        if privacy_date_arr[0]<today_arr[0]:
            answer.append(count)
        elif privacy_date_arr[0]==today_arr[0] and privacy_date_arr[1] < today_arr[1]:
            answer.append(count)
        elif privacy_date_arr[0]==today_arr[0] and privacy_date_arr[1]==today_arr[1] and privacy_date_arr[2] < today_arr[2]:
            answer.append(count)
        count+=1

    return answer