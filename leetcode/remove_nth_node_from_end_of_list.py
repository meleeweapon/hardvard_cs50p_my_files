# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def list_to_linked_list(lst: list) -> Optional[ListNode]:
  head = ListNode(lst[0])
  temp = head
  for obj in lst[1:]:
    temp.next = ListNode(obj)
    temp = temp.next
  return head
def linked_list_to_list(lnkd_lst: Optional[ListNode]) -> list:
  result = []
  temp = lnkd_lst
  while temp != None:
    result.append(temp.val)
    temp = temp.next
  return result


class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    head_pointer = head
    tail_pointer = head
    for _ in range(n):
      tail_pointer = tail_pointer.next

    # means node to be removed is head
    if not tail_pointer:
      return head.next

    while tail_pointer.next:
      head_pointer = head_pointer.next
      tail_pointer = tail_pointer.next

    temp = head_pointer
    head_pointer = head_pointer.next
    temp.next = head_pointer.next
    return head