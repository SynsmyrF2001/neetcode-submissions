class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable):
            if(r, c) in reachable:
                return
            reachable.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)

        # DFS from Pacific borders (top left)
        for r in range(rows):
            dfs(r, 0, pacific_reachable) # Left border
        for c in range(cols):
            dfs(0, c, pacific_reachable) # Top border
        
        # DFS form Atlantic borders (bottom right)
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable) # Right border
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable) # Bottom border

        # Find the intersection
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
        return result
        