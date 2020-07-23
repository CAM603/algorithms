'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# window sequences
[1, 3, -1]
[3, -1, -3]
[-1, -3, 5]
[-3, 5, 3]
[5, 3, 6]
[3, 6, 7]


def sliding_window_max(nums, k):
    my_arr = []

    for i in range(len(nums)):
        if len(nums[i: k + i]) == k:
            my_arr.append(max(nums[i: k + i]))
    return my_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
