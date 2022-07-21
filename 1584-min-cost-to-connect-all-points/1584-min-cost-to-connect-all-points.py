class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        computeWeight = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        getNeighbours = lambda p1: [p for p in range(len(points)) if p != p1 and p not in visited]
        
        visited = set()

        min_cost = 0
        
        min_weight = [(0, (0, 0))]
        
        while len(min_weight):
            weight, (src, dest) = heappop(min_weight)
            if dest not in visited:
                min_cost += weight 
                visited.add(dest)
                src = dest
                for dest in range(len(points)):
                    if dest != src and dest not in visited:
                        weight = (computeWeight(points[src], points[dest]), (src, dest))
                        heappush(min_weight, weight)
        
        return min_cost
        