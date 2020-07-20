# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
# swap helper function
def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    # set is_sorted to show False
    is_sorted = False

    # add a counter variable to help shave time
    counter = 0

    # begin while loop that only runs if the is_sorted remains False
    while not is_sorted:
        # tentatively set is_sorted to True
        is_sorted = True

        # begin for loop that goes until the second-to-last element
        for i in range(len(arr) - 1 - counter):
            # check which element is greater
            if arr[i] > arr[i + 1]:
                # bring in helper swap function
                swap(i, i + 1, arr)

                # and set is_sorted back to false
                is_sorted = False

        # increment counter to tell the next for loop that we don't have to go this far again
        counter += 1

    return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
