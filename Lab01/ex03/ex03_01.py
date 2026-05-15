def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

# Nhập danh sách số nguyên từ người dùng & xử lí chuỗi
input_str = input("Nhập một danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_str.split(',')))
