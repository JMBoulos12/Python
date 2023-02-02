



"""
  You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

  Find two lines that together with the x-axis form a container, such that the container contains the most water.
  Return the maximum amount of water a container can store.
  Notice that you may not slant the container.

  Example 1:
  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49
  Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
  In this case, the max area of water (blue section) the container can contain is 49.
  
  Example 2:
  Input: height = [1,1]
  Output: 1

  Constraints:
  n == height.length
  2 <= n <= 105
  0 <= height[i] <= 104

  02-February-2023
"""


class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    # l_len = len(height)
    # max_area = 0
    # for i in range(l_len - 1):
    #     for j in range(i+1, l_len):
    #         max_area = max(min(height[i], height[j]) * (j - i), max_area)
    # return max_area

    # dup_set = set()
    # tmp_list = []
    # max_index = len(height)
    # for i in range(max_index):
    #     if height[i] in dup_set:
    #         tmp_list.append((height[i], False))
    #     else:
    #         tmp_list.append((height[i], True, i))
    #         dup_set.add(height[i])
    # dup_set = set()
    # final_list = []
    # for i in range(max_index):
    #     idx = max_index - i -1
    #     if tmp_list[idx][0] in dup_set and not tmp_list[idx][1]:
    #         pass
    #     elif tmp_list[idx][0] in dup_set:
    #         dup_set.add(tmp_list[idx][0])
    #         final_list.append((tmp_list[idx][0], idx))
    #     else:
    #         dup_set.add(tmp_list[idx][0])
    #         final_list.append((tmp_list[idx][0], idx))
    # max_area = 0
    # for i in range(len(final_list) - 1):
    #     for j in range(i+1, len(final_list)):
    #         max_area = max(min(final_list[i][0], final_list[j][0]) * (final_list[i][1] - final_list[j][1]), max_area)
    # return max_area
    
    left, right = 0, len(height) - 1
    max_area = min(height[left], height[right]) * (right - left)
    while right > left:
      if height[left] > height[right]:
        right -= 1
        else:
          left += 1
          max_area = max(min(height[left], height[right]) * (right - left), max_area)
          return max_area
