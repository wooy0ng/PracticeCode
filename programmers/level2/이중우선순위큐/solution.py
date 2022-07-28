import heapq


def solution(operations):
    heap = []
    for operation in operations:
        o = operation.split()
        if o[0] == 'I':
            heap.append(int(o[1]))
        elif o[0] == 'D':
            if heap:
                if int(o[1]) > 0:
                    heapq._heapify_max(heap)
                    heapq.heappop(heap)
                else:
                    heapq.heapify(heap)
                    heapq.heappop(heap)
    return [max(heap), min(heap)] if heap else [0, 0]



operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	
print(solution(operations))     # [0,0]
