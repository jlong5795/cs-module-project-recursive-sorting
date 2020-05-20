# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    
    i = 0 # left pointer
    j = 0 # right pointer
    
    for k in range(elements):
        # if we are out of elements on the left
        if i >= len(arrA):
            merged_arr[k] = arrB[j]
            j += 1
        # if we are out of elements on the right
        elif j >= len(arrB):
            merged_arr[k] = arrA[i]
            i += 1
        # if the left is smaller
        elif arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        # if the right is smaller
        else:
            merged_arr[k] = arrB[j]
            j += 1

    return merged_arr
        

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # recursively break the array down
    if len(arr) > 1: # this is our base case
        arrA = merge_sort(arr[:len(arr) // 2]) # slice into two arrays (repeated until len == 1)
        arrB = merge_sort(arr[len(arr) // 2:])

        # call the function to merge them back together
        arr = merge(arrA, arrB)
    return arr

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Treat start->mid and mid-> as though they were separate (but don't separate them)
    # mimics the functionality of merge
    
    # reference to second "part's starting point"
    start2 = mid + 1

    # if already sorted
    if arr[mid] <= arr[start2]:
        return
    
    while start <= mid and start2 <= end:
        # first element is in correct place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            #shift all elements between 1st element and 2nd element right by 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            
            # value is moved to the front of the list
            arr[start] = value

            # increment the pointers
            start += 1
            mid += 1
            start2 += 1


    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = l + (r - l) // 2

        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)

        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
