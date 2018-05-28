# https://stackoverflow.com/questions/18262306/quicksort-with-python


# https://en.wikipedia.org/wiki/Sorting_algorithm
# Quicksort is usually done in-place with O(log n) stack space
# Method: partitioning
# Best: O(nlogn)
# Average: O(nlogn)
# Worst: O(n^2)
# Memory: logn on average, worst case space complexity is n
# Stable: Typical in-place sort is not stable

# https://stackoverflow.com/questions/18262306/quicksort-with-python
def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array