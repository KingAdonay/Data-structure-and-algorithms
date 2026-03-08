class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-1 * stone)

        heapq.heapify(heap)

        while heap:
            if len(heap) == 1:
                return abs(heap[0])

            num1, num2 = heapq.heappop(heap), heapq.heappop(heap)
            num = num1 - num2
            if num:
                heapq.heappush(heap,num)

        return 0
        