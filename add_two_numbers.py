# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        current2 = l2
        list1 = []
        remender = 0
        while current != None and current2 != None:
            # print(current.val, end=" -> ")
            sum = current.val + current2.val
            if sum+remender <=9:
                list1.append(sum+remender)
            elif sum+remender >=10:
                list1.append(sum - 10)
                remender = 1
            current= current.next
            current2= current2.next
        print(list1)            