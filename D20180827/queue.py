import collections

queue = collections.deque()
print(queue)

queue.append("A")
queue.append("B")
queue.append("C")

print(queue)

item1 = queue.popleft()
print(item1)
print(queue)


