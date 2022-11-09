    # 캐시교체 알고리즘 LRU
    # 캐시힛: 메모리가 캐시에 존재하고 있을경우, 실행시간 1
    # 캐시 미스: 메모리가 캐시에 존재하지 않을때, 실행시간 5

def solution(cacheSize, cities):
    cache = []
    ans = 0
    for i in range(len(cities)):
        city = cities[i].lower() # 도시이름 대소문자 바꾼경우도 존재
        if cacheSize > 0:  # 캐시사이즈가 0일경우도 존재
            if len(cache) < cacheSize:  # 처음에 캐시 다 차있을 때 까지 넣기
                if city not in cache:  # 새로들어온 데이터
                    cache.append(city)
                    ans += 5
                else:  # 기존에 있던 데이터
                    idx = cache.index(city)
                    cache.append(cache.pop(idx))
                    ans += 1
            else:  # 캐시가 다 차있다면
                if city not in cache:  # 새로 들어온다면
                    cache.pop(0)
                    cache.append(city)
                    ans += 5
                else:
                    idx = cache.index(city)
                    cache.append(cache.pop(idx))
                    ans += 1
        else:
            ans += 5

    return ans

solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])