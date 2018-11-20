#!/usr/bin/python
def compare_pv(arr,idx):
    """ Compares the current value with previous in the array

        Returns boolean
    """
    return True if idx > 0 and arr[idx] > arr[idx - 1] else False    # Compares values and checks if idx is at beginning

def get_longest_subarray_asc(arr):
    """ Gets longest subarray

        Returns the first longest subarray of ascending order
    """
    if validate_array(arr): return []   # Returns empty array if array not valid

    curr = []
    curr_best = []

    # Compares values in array and retains the current longest subarray
    for idx, val in enumerate(arr):
        if compare_pv(arr,idx):
            curr.append(val)
        else:
            if len(curr) > len(curr_best): curr_best = list(curr)   # Avoids assigning curr_best to curr list object
            curr = [val]

    return curr_best

def get_len_longest_subarray_asc(arr):
    return len(get_longest_subarray_asc(arr))

def validate_array(arr):
    return any(not isinstance(i, (int, float)) for i in arr)    # Validates array for values that aren't a number

if __name__ == "__main__":
    print get_len_longest_subarray_asc([1,4,1,4,2,1,3,5,6,2,3,7])
    print get_len_longest_subarray_asc([3,1,4,1,5,9,2,6,5,3,5])
    print get_len_longest_subarray_asc([2,7,1,8,2,8,1])
