def find_square_root_int(number):
    '''Find the integer value of the square root of a given non-negative whole number.

    Examples:
    find_square_root_int(9) --> 3
    find_square_root_int(8) --> 2 (square root is ~2.828, which as an int is 2)

    Time/Space Complexity of Function (taken from Leetcode):
    Runtime: 12 ms, faster than 98.89% of Python online submissions for Sqrt(x).
    Memory Usage: 11.7 MB, less than 76.12% of Python online submissions for Sqrt(x).
    '''
    if number == 0:
        return 0
    elif number <= 3:
        return 1
    low = 0
    high = number
    while True:
        root = (low+high)//2
        if root*root <= number and (root+1)*(root+1) > number:
            return root
        elif root*root > number:
            high = root
        elif root*root < number:
            low = root

print(find_square_root_int(0)) #0
print(find_square_root_int(1)) #1
print(find_square_root_int(2)) #1
print(find_square_root_int(3)) #1
print(find_square_root_int(4)) #2
print(find_square_root_int(5)) #2
print(find_square_root_int(6)) #2
print(find_square_root_int(7)) #2
print(find_square_root_int(8)) #2
print(find_square_root_int(9)) #3
print(find_square_root_int(10)) #3
print(find_square_root_int(20)) #4
print(find_square_root_int(58)) #7
print(find_square_root_int(399)) #20
print(find_square_root_int(400)) #20
print(find_square_root_int(401)) #20
