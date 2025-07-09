class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #for loop to get the distances list
        for point in points : 
            res = (point[0])**2 + (point[1])**2
            point.insert(0, res)
        
        heapq.heapify(points)
        dist = []
        while k > 0: 
            res, x, y = heapq.heappop(points)
            dist.append([x, y])
            k -= 1
        
        return dist
        