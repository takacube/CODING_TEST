from logging import raiseExceptions

def to_int(input_str):
    sum = 0
    converted_str = ''.join(list(reversed(input_str)))
    for index, each_i in enumerate(converted_str):
        each_i = ten_to_sixteen(each_i)
        sum += 16**(index)*int(each_i)
    print(sum)
    return sum

def ten_to_sixteen(input_str):
    converter = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    if input_str in converter:
        return converter[input_str]
    else:
        return input_str

str = input()
to_int(str)


