# intervals
 + [Non-overlapping Intervals](#non-overlapping-intervals)
 + [Merge Intervals](#merge-intervals)
 
## Non-overlapping Intervals
 https://leetcode.com/problems/non-overlapping-intervals/
 ```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key = lambda x: (x[1]))
    if not intervals:
        return 0
    result = 0
    last_first = intervals[0][0]
    last_second = intervals[0][1]
    for i in range(1,len(intervals)):
        curr_first = intervals[i][0]
        curr_second = intervals[i][1]
        if last_second > curr_first:
            result += 1
        else:
            last_first,last_second = curr_first,curr_second
    return  result

```
## Merge Intervals
 https://leetcode.com/problems/merge-intervals/
 ```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    first = 0
    second = 1
    while first < len(intervals):
        if second >= len(intervals):
            first += 1
            second = first + 1
        elif intervals[first][1] >= intervals[second][0]:
            new = [intervals[first][0],max(intervals[first][1],intervals[second][1])]
            del intervals[second]
            intervals[first] = new
            second = first + 1
        else:
            second += 1
    return intervals

```
