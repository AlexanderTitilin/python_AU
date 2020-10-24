# Array
 + [Squares of a Sorted Array](#squares-of-a-sorted-array)
## Squares of a Sorted Array
 https://leetcode.com/problems/squares-of-a-sorted-array/
 ```python
def sortedSquares(self, A: List[int]) -> List[int]:
    A = list(map(lambda x: x**2,A))
    A.sort()
    return A
    
```