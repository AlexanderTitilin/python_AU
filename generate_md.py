source = open("leetcode/source_leetcode_data.txt")
source = source.readlines()
name = source[0].split(". ")[1][:-1]
link = source[1][:-1]
name_from_link = link.split("https://leetcode.com/problems/")[1][:-1]
code_list=[line[4:] for line in source[3:]]
code = ''.join(code_list)
result = f"\n## {name}\n \
{link}\n \
```python\n\
{code}\n\
```"
file_for_result = open('leetcode/intervals.md', 'a')
file_for_result.write(result)
file_for_result.close();