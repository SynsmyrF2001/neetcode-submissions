class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = []

        for num, freq in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
        
        result = [num for freq, num in heap]

        return result
        