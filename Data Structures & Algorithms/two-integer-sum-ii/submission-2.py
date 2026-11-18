class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers
        # one to first index, next one keeps iterating until value that is just off too big is found also if value is larger than target then skip?
        # try next index, if it doesn't work, continue
        # add check that value isn't the same (if it is, skip)
        # maybe check largest value, so can skip until within bounds

        len_list_index = len(numbers) - 1
        cur_large_val = numbers[len_list_index]
        cur_small_val = numbers[0]
        val_we_want = target - cur_small_val
        pointer1 = 0
        pointer2 = len_list_index

        while cur_large_val != val_we_want:

            if (cur_large_val > val_we_want):
                # if our 'large' value is larger than the val we want,
                # we need a smaller large value
                pointer2 = pointer2 - 1
                last_val = cur_small_val
            else:
                # if the val we want is less than the largest value
                # we need a larger small value
                pointer1 = pointer1 + 1
            
            cur_small_val = numbers[pointer1]
            val_we_want = target - cur_small_val
            cur_large_val = numbers[pointer2]

        return [pointer1+1,pointer2+1]
