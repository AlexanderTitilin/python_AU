#linked-list
 + [Reverse Linked List](#reverse-linked-list)
 + [Middle of the Linked List](#middle-of-the-linked-list)
 + [Palindrome Linked List](#palindrome-linked-list)
 + [Merge Two Sorted Lists](#merge-two-sorted-lists)
 + [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
## Reverse Linked List
 https://leetcode.com/problems/reverse-linked-list/
 ```python
def reverseList(self, head: ListNode) -> ListNode:
    if not head:
        return head
    result = ListNode(head.val)
    head = head.next
    while head:
        result = ListNode(head.val,result)
        head = head.next
    return result
 ```
## Middle of the Linked List
 https://leetcode.com/problems/middle-of-the-linked-list/
 ```python
def middleNode(self, head: ListNode) -> ListNode:
    lenght = 0
    tmp = head
    while tmp:
        lenght += 1
        tmp = tmp.next
    target = lenght // 2
    if lenght == 1:
        return head
    for counter in range(lenght):
        if target - counter == 1:
            return head.next
        head = head.next
 ```
## Palindrome Linked List
 https://leetcode.com/problems/palindrome-linked-list/
 ```python
def isPalindrome(self, head: ListNode) -> bool:
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst == lst[::-1]
```
## Merge Two Sorted Lists
 https://leetcode.com/problems/merge-two-sorted-lists/
 ```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def node_append(lst,elem):
        if not lst:
            return ListNode(elem)
        return ListNode(lst.val,node_append(lst.next,elem))
    result = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            result = node_append(result,l1.val)
            l1 = l1.next
        else:
            result = node_append(result,l2.val)
            l2 = l2.next
    if not l1 and l2:
        while l2:
            result = node_append(result,l2.val)
            l2 = l2.next
    if not l2 and l1:
        while l1:
            result = node_append(result,l1.val)
            l1 = l1.next
    return result.next
```
## Remove Nth Node From End of List
 https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 ```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def node_len(lst):
        counter = 0
        while lst:
            counter += 1
            lst = lst.next
        return counter
    def node_append(lst,elem):
        if not lst:
            return ListNode(elem)
        return ListNode(lst.val,node_append(lst.next,elem))
    result = ListNode()
    n = node_len(head) - n
    counter = 0
    result = ListNode()
    while head:
        if counter != n:
            result = node_append(result,head.val)
        counter += 1
        head = head.next
    return result.next
```