def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # empty dict -- This is where all the comparison with each nums is placed in.
    nums = {}

    # empty list --- This is where my Return Value will be placed in.
    outcome = []

# loops through all the int in the in the list of (a)
    for allnums in a:
        # base case
        if allnums != 0:
            nums[allnums] = 1
            # if base case which ends the loop is not met move to the next condition.

            # when a int is negative in (nums) append with the absolute value.
            if -allnums in nums:
                outcome.append(abs(allnums))
    return outcome


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
