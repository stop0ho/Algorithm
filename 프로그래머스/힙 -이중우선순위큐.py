import heapq as h

def solution(operations):
    heap = []
    max_heap = []
    for i in operations:
        command = i[0]
        if command == "I":
            h.heappush(heap, int(i[2:]))
            h.heappush(max_heap, (-int(i[2:]), int(i[2:])))
        else:
            if len(heap) != 0:
                if i == "D -1":
                    min = h.heappop(heap)
                    max_heap.remove((-min, min))
                else:
                    max = h.heappop(max_heap)[1]
                    heap.remove(max)
    if len(heap) == 0:
        return [0, 0]
    else:
        return [max_heap[0][1], heap[0]]