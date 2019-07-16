def find_closest_number(input_array, target):
    '''
    Description of find_closest_number function taken from YouTube tutorial:
    https://www.youtube.com/watch?v=0gkWZNE1H4Y.

    We will be given a sorted array and a target number. Our goal is to find a
    number in the array that is closest to the target number. We will be making
    use of binary search to solve this problem.

    The array may contain duplicate values and negative numbers.

    Example 1:
        Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
        Target number = 11
        Output : 9
        9 is closest to 11 in given array

    Example 2:
        Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
        Target number = 4
        Output : 5
    '''
    if target <= input_array[0]:
        return input_array[0]
    elif target >= input_array[len(input_array)-1]:
        return input_array[len(input_array)-1]
    low = 0
    high = len(input_array)-1
    while low <= high:
        mid = (low+high)//2
        if target == input_array[mid]:
            return target
        elif target < input_array[mid]:
            if target > input_array[mid-1]:
                if target-input_array[mid-1] < input_array[mid]-target:
                    return input_array[mid-1]
                elif target-input_array[mid-1] > input_array[mid]-target:
                    return input_array[mid]
                else:
                    return target, ": there's a tie"
            high = mid - 1
        elif target > input_array[mid]:
            if target < input_array[mid+1]:
                if input_array[mid+1]-target < target-input_array[mid]:
                    return input_array[mid+1]
                elif input_array[mid+1]-target > target-input_array[mid]-target:
                    return input_array[mid]
                else:
                    return target, ": there's a tie"
            low = mid + 1


print(find_closest_number([1,2,4,5,6,6,8,9],11)) #9
print(find_closest_number([2,5,6,7,8,8,9],4)) #5
