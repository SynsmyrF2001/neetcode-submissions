class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Build adjacency list
        adj = collections.defaultdict(list)
        for u, v, w, in edges:
            adj[u].append((v, w))

        # Init distances w/ inf
        dist = {i: float('inf') for i in range(n)}
        dist[src] = 0

        # Priority queue: (distance, vertex)
        pq = [(0, src)]

        while pq:
            d, u =heapq.heappop(pq)

            # If the extracted distance is greater than the current shortest distance, skip
            if d > dist[u]:
                continue 
            
            # Relax neighbors
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        # Prepare result dictionary, replacing inf with -1 for unreachable verticies
        result = {}
        for i in range(n):
            result[i] = dist[i] if dist[i] != float('inf') else -1 
        
        return result
