# Math
 + [Palindrome Number](#palindrome-number)
 + [Fizz Buzz](#fizz-buzz)
 + [ Base 7](#base-7)
## Palindrome Number
 https://leetcode.com/problems/palindrome-number/
 ```python
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    y = x
    z = 0
    while y != 0:
        z = z*10 + y%10
        y //= 10
    return x == z
```
## Fizz Buzz
 https://leetcode.com/problems/fizz-buzz/
 ```python
def fizzBuzz(self, n: int) -> List[str]:
    result = []
    for i in range(1,n+1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 5 == 0:
            result.append('Buzz')
        elif i % 3 == 0:
            result.append('Fizz')
        else:
            result.append(str(i))
    return result
    
```
## Base 7
 https://leetcode.com/problems/base-7/
 ```python
def convertToBase7(self, num: int) -> str:
    if num == 0:
        return '0'
    result = ''
    sign = 1 if num >= 0 else 0
    num = abs(num)
    while num != 0:
        result = str(num % 7) + result
        num //= 7
    return result if sign else '-'+result
    
```
## Fibonacci Number
 https://leetcode.com/problems/fibonacci-number/
 ```python
def fib(self, N: int) -> int:
    a = [0,1,1]
    if N < 3:
        return a[N]
    for i in range(3,N+1):
        a[0],a[1],a[2] = a[1],a[2],a[1] + a[2]
    return a[2]
    
```