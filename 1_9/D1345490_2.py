def two_sum(nums, target):
    seen = {}  

    for i, num in enumerate(nums):
        remain = target - num
        if remain in seen:
            return (seen[remain], i)
        seen[num] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))