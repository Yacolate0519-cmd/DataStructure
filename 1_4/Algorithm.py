import random

# def merge_sort(data):
#     if len(data) <= 1:
#         return data

#     mid = len(data) // 2
#     left = data[:mid]
#     right = data[mid:]

#     left_sorted = merge_sort(left)
#     right_sorted = merge_sort(right)

#     return merge(left_sorted, right_sorted)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])        
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# def bubble_sort(data):
#     for i in range(len(data)):
#         for j in range(i, len(data)):
#             if data[i] > data[j]:
#                 data[i], data[j] = data[j], data[i]
#     return data

# def quick_sort(data):
#     if len(data) <= 1:
#         return data
#     else:
#         pivot = data[len(data) // 2]
#         left = []
#         right = []
#         left = [i for i in data if i < pivot]
#         right = [i for i in data if i > pivot]
#         return quick_sort(left) + [pivot] + quick_sort(right)

# def selection_sort(data):
    # sorted_data = []
    # min_value = data[0]
    # for i in data:
    #     pass
    #     sorted_data.append(min_value)
    # return sorted_data

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data

def merge_sort(data):
    if len(data) == 1:
        return data
    mid = len(data) // 2    
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[len(data) // 2]
        left = [i for i in data if i < pivot]
        right= [i for i in data if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    data = [i for i in range(10)]
    random.shuffle(data)
    print(data)

    # sorted_data = bubble_sort(data)
    # sorted_data = merge_sort(data)
    # sorted_data = quick_sort(data)
    # sorted_data = selection_sort(data)

    sorted_data = sorted(data)

    print(sorted_data)