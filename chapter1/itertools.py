from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement


data1 = ['A', 'B', 'C']
result1 = list(permutations(data1, 3))
print(result1)

data2 = ['D', 'E', 'F']
result2 = list(combinations(data2, 2))
print(result2)

data3 = ['A', 'B', 'C']
result3 = list(product(data3, repeat=3))
print(result3)

data4 = ['D', 'E', 'F']
result4 = list(combinations_with_replacement(data4, 2))
print(result4)