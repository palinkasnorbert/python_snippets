def create_staircase(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


nums = [1, 2, 3, 4, 5, 6]
step = 1
subsets = []
print(nums[0])
print(nums[1])
subsets.append(nums[0:step])
print(subsets)
