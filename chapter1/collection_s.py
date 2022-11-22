from collections import deque
from collections import Counter


data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['red'])
print(counter['green'])

print(dict(counter))