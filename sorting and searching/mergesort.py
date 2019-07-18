def merge_sort(input_array):
    '''
    Sort input_array using the "merge sort" sorting algorithm

    Time Complexity (worst-case): O(n*logn) - ... (fill in)

    Space Complexity (worst-case): O(n) - ... (fill in)
    '''
    if len(input_array) < 2:
        return input_array
    lefthalf = merge_sort(input_array[:len(input_array)//2])
    righthalf = merge_sort(input_array[len(input_array)//2:])
    return merge(lefthalf, righthalf)

def merge(lefthalf, righthalf):
    '''
    Helper function for merge_sort that merges the left and right array halves
    '''
    output_array = []
    l = 0
    r = 0
    while l < len(lefthalf) and r < len(righthalf):
        if lefthalf[l] < righthalf[r]:
            output_array.append(lefthalf[l])
            l += 1
        else:
            output_array.append(righthalf[r])
            r += 1
    output_array += lefthalf[l:]
    output_array += righthalf[r:]
    return output_array

arr1 = [8,3,1,7,0,10,2]
arr2 = [21,4,1,3,9,20,25,22,17,2,8]
arr1 = merge_sort(arr1)
arr2 = merge_sort(arr2)
print(arr1) #0,1,2,3,7,8,10
print(arr2) #1,2,3,4,8,9,17,20,21,22,25
