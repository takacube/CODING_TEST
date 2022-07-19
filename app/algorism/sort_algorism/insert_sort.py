def insert_sort(data):
    for insert_index in range(1, len(data)):
        to_be_inserted = data[insert_index]
        compared_index = insert_index - 1
        while (compared_index >= 0) and (data[compared_index] > to_be_inserted):
            data[compared_index+1] = data[compared_index]
            compared_index -= 1
            data[compared_index] = to_be_inserted
    return data

list = [1, 3, 7, 2, 4, 18, 4, 3]
sorted_list = insert_sort(list)
print(sorted_list)


