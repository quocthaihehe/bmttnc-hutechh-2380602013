# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))

# Kiểm tra xem số chẵn hay lẻ
if so % 2 == 0:
    print("Số", so, "là số chẵn.") 
else:
    print("Số", so, "Không phải là số chẵn.")