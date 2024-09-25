list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [[7, 8, 9], [10, 11, 12]]

add = [[a + b for a, b in zip(sublist1, sublist2)] for sublist1, sublist2 in zip(list1, list2)]
print(add)  # Output: [[8, 10, 12], [14, 16, 18]]
