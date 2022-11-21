# 1 : sum()
sum_result = sum([1, 2, 3, 4, 5])
print(sum_result)

# 2 : min()
min_result = min(7, 3, 5, 2)
print(min_result)

# 3 : max()
max_result = max(14, 2, 5, 8)
print(max_result)

# 4 : eval()
eval_result = eval("(17+32) / 7")
print(eval_result)

# 5: sorted()
sorted_result = sorted([9, 1, 8, 4, 5])
print(sorted_result)

reverse_result = sorted(sorted_result, reverse = True)
print(reverse_result)

# 5-2: sorted() + key
list_result = sorted([("홍길동", 35), ("아무개", 50), ("이순신", 75)], key = lambda x: x[1], reverse = True)
print(list_result);


# 6: sort()
data = [9, 1, 8, 5, 4]
data.sort()
print(data)

