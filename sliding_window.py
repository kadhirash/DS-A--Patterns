'''
1) Find the max sum subarray of a fixed size K

Example: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
'''

# Problem: 1


def find_max_subarray(arr, k):
    max_sum, window_sum = 0, 0
    window_start = 0

    if k <= 0:
        return None
    # starting from window_end --> end of array
    for window_end in range(len(arr)):
        # add next element in 'window' to the window sum
        window_sum += arr[window_end]
        # is window sum > max sum?. # window_sum = how far in array, k-1 = end index in 'window' (3 elements; 2nd index in this case)
        if window_end >= k-1:
            # set max sum to max value between max_sum vs the window_sum
            max_sum = max(max_sum, window_sum)
            # subtract element going out
            window_sum -= arr[window_start]
            # slide 'window'
            window_start += 1
    return max_sum


'''
2) Find the smallest subarray with given sum

Example: [[4, 2, 2, 7, 8, 1, 2, 8, 10]
'''


def smallest_subarray(arr, target_sum):
    # set min length to some really high # (positive inf)
    min_length = float('inf')
    window_sum = 0
    window_start = 0
    if target_sum == 0:  # if target sum = 0
        return 0
    if target_sum <= 0:  # numbers less than 0, return none
        return None
    for window_end in range(len(arr)):
        # window sum adds next elem until the window_end
        window_sum += arr[window_end]
        # shrink window until 'window sum' < 'target_sum'
        while window_sum >= target_sum:
            min_length = min(  # now find min of min_window_size and window_end - window_start + 1
                min_length, (window_end - window_start + 1))
            # window sum subtracted from the window start b/c getting rid of it
            window_sum -= arr[window_start]
            # while target sum satisifed, minimize the left side
            window_start += 1
    return min_length


'''
3) Longest substring with k distinct

Example: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
'''


def longest_substring_with_k_distinct(string, k):
    # initialize variables and dict
    window_start = 0
    max_length = 0
    frequency_char = {}

    # extend range [window_start], [window_end]
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in frequency_char:
            frequency_char[right_char] = 0
        frequency_char[right_char] += 1

        # shrink window until left with 'k' distinct chars in freq_char
        while len(frequency_char) > k:
            left_char = string[window_start]
            frequency_char[left_char] -= 1
            if frequency_char[left_char] == 0:
                del frequency_char[left_char]
            # shrink window
            window_start += 1
        max_length = max(max_length, (window_end - window_start + 1))
    return max_length


def main():
    # Problem: 1
    arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
    k = 8
    print(find_max_subarray(arr, k))

    # Problem: 2
    arr = [4, 2, 2, 7, 8, 1, 2, 8, 10]
    target_sum = 4
    print(smallest_subarray(arr, target_sum))

    # Problem: 3
    string1 = 'a', 'b', 'd', 'e', 'r', 'r'
    k1 = 4
    string2 = ''
    k2 = -1
    print(longest_substring_with_k_distinct(string1, k1))
    print(longest_substring_with_k_distinct(string2, k2))


main()
