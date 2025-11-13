from combine import combine as cx
def combine_sort(unsorted):
    unsorted=[5,4,3,2,1]
    size = len(unsorted)

    left = unsorted[0:1]
    for idx in range(1,size):
        right= unsorted[idx: idx+1]
        left = cx(left,right)

    return left