



"""
  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

  Merge all the linked-lists into one sorted linked-list and return it.

  Example 1:
  Input: lists = [[1,4,5],[1,3,4],[2,6]]
  Output: [1,1,2,3,4,4,5,6]
  Explanation: The linked-lists are:
  [
    1->4->5,
    1->3->4,
    2->6
  ]
  merging them into one sorted list:
  1->1->2->3->4->4->5->6
  
  Example 2:
  Input: lists = []
  Output: []
  
  Example 3:
  Input: lists = [[]]
  Output: []

  Constraints:
  * k == lists.length
  * 0 <= k <= 104
  * 0 <= lists[i].length <= 500
  * -104 <= lists[i][j] <= 104
  * lists[i] is sorted in ascending order.
  * The sum of lists[i].length will not exceed 104. 
  
  08-February-2023
"""

from queue import PriorityQueue

class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    pq = PriorityQueue()

    for i, lst in enumerate(lists):
      if lst:
        pq.put((lst.val, i, lst))

    while not pq.empty():
      _, i, minNode = pq.get()
      if minNode.next:
        pq.put((minNode.next.val, i, minNode.next))
      curr.next = minNode
      curr = curr.next

    return dummy.next
