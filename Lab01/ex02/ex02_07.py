# Nhập các dòng từ user
print("Nhập các dòng văn bản (nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
# Chuyển các dòng thành chữ in hoa và in ra
print("\nCác dòng đã chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())