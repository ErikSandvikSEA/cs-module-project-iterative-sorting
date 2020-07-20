# swap helper function
def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # declare the current_idx at the start of the arr [0]
    current_idx = 0

    # create a while loop for the entire list
    while current_idx < len(arr) - 1:
        # initialize the smallest element's index as the one we're currently on.
        # It will likely get changed during the for loop
        smallest_elem_idx = current_idx
        # build for loop that spans the list from the current_idx to the end of the array
        for i in range(current_idx, len(arr)):
            # compare the smallest_elem_idx that we currently have to the element of this pass of the for loop
            # if the for loop element is smaller, set that to the smallest_elem_idx
            if arr[i] < arr[smallest_elem_idx]:
                smallest_elem_idx = i

        # swap whichever element we have marked as the smallest with the one we're currently looking at
        swap(current_idx, smallest_elem_idx, arr)

        # iterate up the current_idx for the next for loop
        current_idx += 1

    return arr


# TO-DO:  implement the Bubble Sort function below


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
