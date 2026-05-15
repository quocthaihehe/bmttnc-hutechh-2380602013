def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập danh sách số nguyên từ người dùng & xử lí chuỗi
input_str = input("Nhập một danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_str.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List:" , numbers)
print("Tuple từ list:", my_tuple)