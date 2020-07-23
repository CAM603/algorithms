'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# How many are in the list?
# Start with i at the first item
# Send a cursor j down the list
# if j finds an item that matches i, that is not what we are looking for
# # increment i and send j down the list
# if j reaches the end and nothing matches i, i is the number to return


def single_number(arr):
    # Your code here
    dic = {}
    for num in arr:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    for num in set(arr):
        if dic[num] == 1:
            return num
    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
