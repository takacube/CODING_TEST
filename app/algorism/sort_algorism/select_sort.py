def select_sort(data):
    for axis in range(len(data)):
        min_ = axis
        for compared_index in range(axis+1, len(data)):
            if data[compared_index] < data[min_]:
                min_ = compared_index
                data[axis], data[min_] = data[min_], data[axis]
    return data

list = [1, 4, 17, 2, 8, 1]
sorted_list = select_sort(list)
print(sorted_list)
