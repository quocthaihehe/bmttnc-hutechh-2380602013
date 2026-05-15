def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Nhập ds từ user
input_str = input("Nhập một danh sách (cách nhau bởi dấu phẩy): ")
word_list = input_str.split()

# Sử dụng hàm & in ra kq
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của mỗi phần tử:", so_lan_xuat_hien)   
