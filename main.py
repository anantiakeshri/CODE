
""" BIG O notation"""

# # 1. O(n)
# def print_item(n):
#     for i in range(n):
#         print(i)
        
# print(print_item(10))


# # 2. O(n^2)
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)
            
# print(print_items(10))


# 3. O(1) - constant time - most efficient
def print_item(n):
    return n + n + n

print(print_item(10))

# 4. O(log n) - more efficient than O(n) and O(n^2)
# 5. O(n log n) -  For some sorting algorithm
