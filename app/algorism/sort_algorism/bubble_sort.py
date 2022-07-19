def bubble_sort(data):
    for order in range(len(data)):
        #print(f"一つ目のfor:{order}")
        for index in range(len(data)-order-1):
            print(f"2つ目のfpr{index}")
            if data[index] > data[index+1]:
                data[index], data[index+1] = data[index+1], data[index]
    return data

list = [2, 3, 14, 2, 9, 12]
sorted_list = bubble_sort(list)
print(sorted_list)
