import heapq

# 1
def heapsort(iterable) :
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 (최상위 원소부터)
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result);

# 2 : 최대 힙(Max Heap) 구현하기
# ✅ 원소 부호 변경
def m_heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable :
        heapq.heappush(h, -value)
        # 0, -1, -2, -3, ... (역순으로 삽입됨)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 (최상위 원소부터)
    for i in range(len(h)) :
        result.append(-heapq.heappop(h))
        # 다시 꺼낼 때에는 부호 바꾸어서!
    return result
result2 = m_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result2);
