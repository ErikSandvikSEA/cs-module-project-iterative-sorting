def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
# def binary_search(arr, target):
# declare a left variable for the 1st element, and a right variable for the last
# left = 0
# right = len(arr) - 1

# # do a while loop for as long as the left variable is equal or less than the right
# # overlapping is fine, but no passing
# while left <= right:
#     # declare a midpoint variable that floors to the lowest integer (if float)
#     mid = (right + left) // 2

#     # check if the mid element matches the target, if so, we win !
#     if arr[mid] == target:
#         return mid

#     # check if the mid element is higher than the target
#     elif arr[mid] > target:
#         # then set the right pointer to the mid - 1
#         right = mid - 1

#     # and vice versa
#     else:
#         left = mid + 1

# return -1  # not found
