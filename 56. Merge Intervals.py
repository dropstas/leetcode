class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        array = []
        cell = [0, 0]
        end = max(intervals[0])
        start = min(intervals[0])
        for i in intervals:
            if min(i) >= start and max(i) <= end:
                pass 
            elif end >= min(i) and end <= max(i):
                end = max(i)
            else:
                array.append(cell)
                end = max(i)
                start = min(i)
                
            cell = [start, end]

        array.append(cell)

        return array