'''
1) Find the max sum subarray of a fixed size K

Example: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
'''

# Problem: 1


def find_max_subarray(arr, k):
    max_val = float('-inf')  # set max. value to really low # (negative inf)
    curr_running_sum = 0

    # starting from 0 --> end of array
    for i in range(len(arr)):
        # add values in 'window' to the current running sum
        curr_running_sum += arr[i]
        # is current running sum > max value?. # i = how far in array, k-1 = end index in 'window' (3 elements; 2nd index in this case)
        if i >= k-1:
            # set max value to max value between current running sum vs the max value
            max_val = max(max_val, curr_running_sum)
            # subtract furthest left value so we can (shift 'window')
            curr_running_sum -= arr[i - (k-1)]

    return max_val


'''
2) Find the smallest subarray with given sum

Example: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
'''


def smallest_subarray(arr, target_sum):
    # set min window size to some really high # (positive inf)
    min_window_size = float('inf')
    curr_window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        # current window sum adds values until the window_end
        curr_window_sum += arr[window_end]

        while curr_window_sum >= target_sum:
            if curr_window_sum == target_sum:  # if current window sum == target sum
                min_window_size = min(  # now find min of min_window_size and window_end - window_start + 1
                    min_window_size, (window_end - window_start + 1))
            # current window sum subtracted from the window start b/c getting rid of it
            curr_window_sum -= arr[window_start]
            # while target sum satisifed, minimize the left side
            window_start += 1
    return min_window_size


def main():
    # Problem: 1
    arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    k = 3
    print(find_max_subarray(arr, k))

    # Problem: 2
    arr = [4, 2, 2, 7, 8, 1, 2, 8, 10]
    target_sum = 20
    print(smallest_subarray(arr, target_sum))


main()
