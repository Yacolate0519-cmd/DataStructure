def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[-1]          
    left = []
    right = []
    for i in range(len(nums) - 1):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    result = quick_sort(nums)
    print(result)