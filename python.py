import itertools

c=itertools.groupby(sorted([(a, b) for a in range(4) for b in range(4)], key=lambda x:x[0]+x[1]), key=lambda x:x[0]+x[1])
>>> for k, g in c:
    print "%s : %s"%(k, [a for a in g])
<<<
0 : [(0, 0)]
1 : [(0, 1), (1, 0)]
2 : [(0, 2), (1, 1), (2, 0)]
3 : [(0, 3), (1, 2), (2, 1), (3, 0)]
4 : [(1, 3), (2, 2), (3, 1)]
5 : [(2, 3), (3, 2)]
6 : [(3, 3)]


# Cartesian product of input iterables:
product = lambda lst: reduce(lambda a, b:[x+[y] for x in a for y in b], lst, [[]])

product([[1,2], [3,4]])
>>>
[[1, 3], [1, 4], [2, 3], [2, 4]]

#######################################
# distribute n into k part, generate all unique permutation
def generate(k, n):
	res = []
	for i in range(1, n+1, 1):
		findX(res, [i], 1, k, i, n)
	return res

def findX(res, cur_list, already_find_elem, total_elem, already_taken_place, total_place):
	if already_taken_place==total_place:
		if already_find_elem == total_elem:
			res.append(list(cur_list))
		return
	for i in range(cur_list[-1], total_place - already_taken_place + 1, 1):
		cur_list.append(i)
		findX(res, cur_list, already_find_elem+1, total_elem, already_taken_place+i, total_place)
		cur_list.pop()


#######################################
import heapq
def findMin(lst):
    n = len(lst)
    candidate_queue = [[lst[i][0], 0, i] for i in range(n)]
    heapq.heapify(candidate_queue)
    max_edge = max(candidate_queue)[0]
    res = [candidate_queue[0][0], max_edge]
    while True:
    	candidate_res = [candidate_queue[0][0], max_edge]
    	if (candidate_res[1] - candidate_res[0] < res[1] - res[0]) or (candidate_res[1] - candidate_res[0] == res[1] -res[0] and candidate_res[0] < res[0]):
    		res = candidate_res
    	smallest = heapq.heappop(candidate_queue)
    	smallest[1] += 1
    	if smallest[1] == len(lst[smallest[2]]):
    		break
    	else:
    		smallest[0] = lst[smallest[2]][smallest[1]]
    		max_edge = max(max_edge, smallest[0])
    		heapq.heappush(candidate_queue, smallest)
    return res



######  Quick Sort  #####################
def quicksort(nums):
    quicksort_helper(nums, 0, len(nums)-1)
    print nums

# version 1
def quicksort_helper(nums, i, j):
    if i>=j:
        return
    pivot = nums[i]
    idx, idy = i+1, j
    while idx < idy:
      if nums[idx]<pivot:
        idx += 1
      else:
        nums[idx], nums[idy] = nums[idy], nums[idx]
        idy -= 1
    mid_idx = 0
    if nums[idx] >= pivot:
      nums[i], nums[idx-1] = nums[idx-1], nums[i]
      mid_idx = idx-1
    else:
      nums[i], nums[idx] = nums[idx], nums[i]
      mid_idx = idx
    quicksort_helper(nums, i, mid_idx-1)
    quicksort_helper(nums, mid_idx+1, j)

# version 2
def quicksort_helper(nums, i, j):
  if i >= j:
    return
  pivot = nums[i]
  next_hi = j
  scan_ptr = j
  for scan_ptr in range(j, i, -1):
    if nums[scan_ptr] >= pivot:
      nums[next_hi], nums[scan_ptr] = nums[scan_ptr], nums[next_hi]
      next_hi -= 1
  nums[i], nums[next_hi] = nums[next_hi], nums[i]
  print nums


#######################################

class CircularQueue():
  def __init__(self, size):
    self.size = size
    self.queue = [None for i in range(size)]
    # front point: represent empty queue when equals -1
    self.front = -1
    self.rear = 0
  def enqueue(self, data):
    # when front point is just one step ahead of rear, it means queue is full
    if (self.rear+1)%self.size == self.front:
      print("Queue is Full")
    # when queue is empty
    elif self.front == -1:
      self.queue[self.rear] = data
      self.front = self.rear
    else:
      self.rear = (self.rear+1)%self.size
      self.queue[self.rear] = data
  def dequeue(self):
    if self.front == -1:
      return None
    ans = self.queue[self.front]
    # when front == rear, it means there is only one element
    if self.front == self.rear:
      self.front = -1
    else:
      self.front = (self.front+1)%self.size
    return ans

cc = CircularQueue(3)
cc.enqueue(1)
cc.enqueue(2)
cc.enqueue(3)
cc.enqueue(4)
cc.dequeue()
cc.dequeue()
cc.dequeue()
cc.dequeue()
cc.enqueue(1)
cc.enqueue(2)
cc.dequeue()
cc.dequeue()

#######################################
from collections import OrderedDict
class Marathon():
  def __init__(self):
    # sensor_map stores the information that for each sensor, who has passed
    self.sensor_map = {}
    # runner_map stores the information that for each runner, how many (which fartest) sensor has passed
    self.runner_map = {}
    # max_sensor_passed give us information to retrive the head of line
    self.max_sensor_passed = 0

  def signal(self, runner_id):
    passed_sensor = 0 if runner_id not in self.runner_map else self.runner_map[runner_id]
    if passed_sensor in self.sensor_map:
      del self.sensor_map[passed_sensor][runner_id]
    if (passed_sensor+1) not in self.sensor_map:
      self.sensor_map[passed_sensor+1] = OrderedDict()
    self.runner_map[runner_id] = passed_sensor+1
    self.sensor_map[passed_sensor+1][runner_id] = None
    self.max_sensor_passed = max(self.max_sensor_passed, passed_sensor+1)

  def getTopK(self, k):
    ans = []
    for i in range(self.max_sensor_passed, 0, -1):
      if i not in self.sensor_map:
        continue
      runner = self.sensor_map[i]
      for runner_id in runner.keys():
        ans.append(runner_id)
        if len(ans)==k:
          return ans
    return ans


#######################################
from binarytree import Node
import random

class solution(object):
  def create(self, A):
    node_list = [] 
    for a in A:
      node = Node(a)
      root = None
      while  node_list and node_list[-1].value < a:
        node_list[-1].right = root
        root = node_list.pop()
      node.left = root
      node_list.append(node)
    root = None
    while node_list:
      node_list[-1].right = root
      root=node_list.pop()
    return root
  def test(self, A):
    print A
    print self.create(A)


s = solution()
a = [1,2,3,6,5,4]
s.test(a)




