class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)

        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return [[r, c] for r, c in pacific & atlantic]