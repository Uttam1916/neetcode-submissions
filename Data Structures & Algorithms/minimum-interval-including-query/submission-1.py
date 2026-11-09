class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res=dict()
        initial = queries.copy()
        queries.sort()
        intervals.sort()
        h=[]
        i=0
        for k in range(len(queries)):
            while i < len(intervals) and queries[k]>=intervals[i][0]:
                heapq.heappush(h,[intervals[i][1]-intervals[i][0]+1,intervals[i][1]])
                i+=1

            while h and h[0][1]<queries[k]:
                heapq.heappop(h)
                
            if len(h)==0:
                res[queries[k]]=-1
            else:
                res[queries[k]]=h[0][0]

        output=[]
        for n in initial:
            output.append(res[n])

        return output