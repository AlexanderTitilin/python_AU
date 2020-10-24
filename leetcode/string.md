#string
 + [Valid Anagram](#valid-anagram)
 + [Reverse String](#reverse-string)
 +[ Reverse Vowels of a String](#reverse-vowels-of-a-string)
## Valid Anagram
 https://leetcode.com/problems/valid-anagram/
 ```python
def isAnagram(self, s: str, t: str) -> bool:
    s_counter = [0]*27
    t_counter = [0]*27
    for i in s:
        s_counter[ord(i) - 96] +=1
    for i in t:
        t_counter[ord(i) - 96] +=1
    return s_counter == t_counter

```
## Reverse String
 https://leetcode.com/problems/reverse-string/
 ```python
def reverseString(self, s: List[str]) -> None:
    for i in range(len(s)):
        s.insert(i,s.pop(len(s) - 1))
        
        
        
```
## Reverse Vowels of a String
 https://leetcode.com/problems/reverse-vowels-of-a-string/
 ```python
def reverseVowels(self, s: str) -> str:
    vowels = "aeiouAEIOU"
    s = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i+=1
        if s[j] not in vowels:
            j-=1
        if s[i] in vowels and s[j] in vowels:
            s[i],s[j] = s[j],s[i]
            j-=1
            i+=1
    return "".join(s)
        
        
```

## To Lower Case
 https://leetcode.com/problems/to-lower-case/
 ```python
def toLowerCase(self, str: str) -> str:
    result = ''
    for i in str:
        if ord(i) > 64 and ord(i) < 91:
            result += chr(ord(i) + 32)
        else:
            result += i
    return result
```
## Squares of a Sorted Array
 https://leetcode.com/problems/squares-of-a-sorted-array/
 ```python
def sortedSquares(self, A: List[int]) -> List[int]:
    A = list(map(lambda x: x**2,A))
    A.sort()
    return A
    
```
## Squares of a Sorted Array
 https://leetcode.com/problems/squares-of-a-sorted-array/
 ```python
def sortedSquares(self, A: List[int]) -> List[int]:
    A = list(map(lambda x: x**2,A))
    A.sort()
    return A
    
```