def decode(target):
    for i in range(target // 2):
        if i ** 2 <= target and (i + 1) ** 2 > target:
            return i

if __name__ == '__main__':
    target = 17
    target = int(target)
    print(decode(target))