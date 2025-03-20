def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city_low = city.lower()
        if cacheSize == 0:
            answer+=5
        else:
            if city_low in cache:
                answer+=1
                cache.remove(city_low)
                cache.append(city_low)
            else:
                answer+=5
                if len(cache) == cacheSize:
                    cache.pop(0)
                    cache.append(city_low)
                else:
                    cache.append(city_low)
    return answer