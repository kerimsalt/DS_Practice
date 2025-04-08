def max_consecutive_odd_numbers(nums: list):
    max_len = 0
    curr = 0
    for num in nums:
        if num % 2 == 1:
            curr += 1
        else:
            curr = 0
        max_len = max(max_len, curr)
    return max_len


def longest_subarray_with_two_parity_blocks(nums: list):
    even = [0] * len(nums)
    odd = [0] * len(nums)
    max_parity = [0] * len(nums)
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    if nums[0] % 2 == 0:
        even[0] = 1
        prev = 0  # previous parity (0: even, 1: odd)
        curr = 0  # current parity
    else:
        odd[0] = 1
        prev = 1
        curr = 1

    max_parity[0] = 1
    mp = 0
    for i in range(1, len(nums)):
        prev = curr
        curr = nums[i] % 2
        if nums[i] % 2 == 0:
            if prev != curr:  # check for parity change
                even[i] = 1
            else:
                even[i] = even[i - 1] + 1
            odd[i] = odd[i - 1]
        else:
            if prev != curr:  # check for parity change
                odd[i] = 1
            else:
                odd[i] = odd[i - 1] + 1
            even[i] = even[i - 1]
        max_parity[i] = even[i] + odd[i]
        mp = max(mp, max_parity[i])
    return mp


print(longest_subarray_with_two_parity_blocks([2, 4, 6, 1, 3, 5, 2, 4]))  # 6
print(longest_subarray_with_two_parity_blocks([1, 3, 5, 7, 9]))  # 5
print(longest_subarray_with_two_parity_blocks([1, 2, 3, 4, 5]))  # 2
