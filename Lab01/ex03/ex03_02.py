def dao_nguoc_list(lst):
    return lst[::-1]

# Nhập danh sách số nguyên từ người dùng & xử lí chuỗi
input_str = input("Nhập một danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_str.split(',')))

# Sử dụng hàm để in ra danh sách đảo ngược
list_dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách đảo ngược là:", list_dao_nguoc)
