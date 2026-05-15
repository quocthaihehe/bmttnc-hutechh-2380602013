def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
# Sử dụng hàm để nhập chuỗi và in ra chuỗi đảo ngược
input_str = input("Nhập một chuỗi: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_str))