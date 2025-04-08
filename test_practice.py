from practice import longest_subarray_with_two_parity_blocks


def test_longest_subarray_with_two_parity_blocks():
    test_cases = [
        ([1, 3, 5, 7, 9], 5),           # All odd
        ([2, 4, 6, 8, 10], 5),          # All even
        ([2, 4, 6, 1, 3, 5], 6),        # 2 blocks
        ([2, 4, 6, 1, 3, 5, 2, 4], 6),  # 3 blocks
        ([1, 2, 3, 4, 5], 2),           # alternating
        ([7], 1),                       # one element
        ([], 0),                        # empty array
        ([2, 4, 1, 3, 2, 4, 6], 5),     # edge case
        ([1, 2, 3, 4, 5, 6, 7, 8], 2),  # 4 blocks
        ([2, 1, 2, 1, 2, 1], 2),        # alternating
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = longest_subarray_with_two_parity_blocks(nums)
        assert result == expected, f"❌ Test case {i} failed: expected {expected}, got {result}"
        print(f"✅ Test case {i} passed: expected {expected}, got {result}")

    print("🎉 All test cases passed!")


test_longest_subarray_with_two_parity_blocks()
