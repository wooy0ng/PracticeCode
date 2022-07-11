import heapq
def solution(scoville, K):
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    get_scoville = lambda a, b: a + (b * 2)
    heap = scoville.copy()
    heapq.heapify(heap)
    scoville_rate = 0
    cnt = 0
    while True:
        if len(heap) < 2:
            if heap[-1] < K:
                return -1
            else:
                break
        pop = [heapq.heappop(heap) for _ in range(2)]
        if pop[0] >= K:
            break
        scoville_rate = get_scoville(*pop)
        cnt += 1
        if scoville_rate < K and not heap:
            return -1
        heapq.heappush(heap, scoville_rate)
    return cnt

scoville = [1, 2, 3, 4, 5]	
k = 50
print(solution(scoville, k))