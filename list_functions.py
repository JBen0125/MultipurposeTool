"""
Classes:

        list_functions

Functions:

        sort_list(array)                    # Used
        sum_list(array)                     # Used
        mean_list(array)                    # Used
        median_list(array)                  # Used
        mode_list(array)                    # Used
"""


def sort_list(array):
    """
    Sort List is an example of Bubble Sort 
    which has a worst case time complexity 
    of O(n^2).
    """
    if len(array) == 0:
        return array

    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
    return array


def sum_list(array):
    """
    Sum List is an algorithm that sums up
    all the items in the array, primarily
    used as a helper function, this algorithm
    has a worst case time complexity of O(n).
    """
    if len(array) == 0:
        return None

    summation = 0
    for item in array:
        summation += item
    return summation


def mean_list(array):
    """
    Mean List is an algorithm that takes the
    mean of the array, this algorithm uses the
    Sum List function, therefore the worst case
    time complexity is O(n).
    """
    if len(array) == 0:
        return None

    if sum_list(array) % len(array) == 0:
        return sum_list(array) // len(array)
    return sum_list(array) / len(array)


def median_list(array):
    """
    Median List finds the value exactly in the
    middle of the array, this algorithm uses 
    Sort List, therefore the worst case time
    complexity is O(n^2).
    """
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]
    
    sort_list(array)
    if len(array) % 2 != 0:
        return array[(len(array) // 2) + 1]
    else:
        return (array[(len(array) // 2) - 1] + array[(len(array) // 2)]) / 2


def mode_list(array):
    """
    Mode List finds the most common value in
    the array, this algorithm uses Sort List
    as well as a while loop, therefore the
    worst case time complexity will be O(n^2 * log(n)).
    """
    if len(array) == 0:
        return None
    
    tmp = 1
    mode = array[0]
    count = 1
    sort_list(array)
    i = 1
    while i < len(array):
        if array[i] == array[i-1]:
            count += 1
            if tmp < count:
                tmp = count
                mode = array[i-1]
        else:
            count = 1
        i += 1
    return mode


if __name__ == "__main__":
    ali = [5, 10, 7, 8, 10, 8, 10, 6, 9, 10]
    print("sorted:\t\t{0}\nsum:\t\t{1}\nmean:\t\t{2}\nmedian:\t\t{3}\nmode:\t\t{4}\n".format(sort_list(ali), 
        sum_list(ali), mean_list(ali), median_list(ali), mode_list(ali)))
