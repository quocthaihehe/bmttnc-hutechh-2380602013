from QLSinhVien import QLSinhVien 

qlsv = QLSinhVien()
while True:
    print("\n CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("************************************************************")
    print("1. Thêm sinh viên.                                   *******")
    print("2. Cập nhật thông tin sinh viên theo ID.             *******")
    print("3. Xoá sinh viên theo ID.                            *******")
    print("4. Tìm kiếm sinh viên theo tên.                      *******")
    print("5. Sắp xếp sinh viên theo điểm trung bình.           *******")
    print("6. Sắp xếp sinh viên theo ngành.                     *******")
    print("7. Hiển thị danh sách sinh viên.                     *******")
    print("0. Thoát                                             *******")


    key = int(input("Nhập tuỳ chọn (0-7) : "))
    if (key == 1):
        print("\n1. Thêm sinh viên")
        qlsv.nhapSV()
        print("\nThêm sinh viên thành công!")
        
    elif (key == 2):
        if(qlsv.soLuongSV() > 0):
            print("\n2. Cập nhật thông tin sinh viên")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSV(ID)
        else:
            print("\nKhông có sinh viên nào để cập nhật thông tin!")
            
    elif (key == 3):
        if(qlsv.soLuongSV() > 0):
            print("\n3. Xoá sinh viên")
            print("\nNhập ID: ")
            ID = int(input())
            if(qlsv.deleteID(ID)):
                print("\nSinh viên có ID: ", ID, " đã được xoá thành công!")
            else:
                print("\nSinh viên có ID: ", ID, " không tồn tại!")
        else:
            print("\nKhông có sinh viên nào để xoá!")
        
    elif (key == 4):
        if(qlsv.soLuongSV() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên")
            print("\nNhập tên: ")
            name = input()
            searchResults = qlsv.findByName(name) # Sửa lỗi thiếu tham số ()
            qlsv.showListSV(searchResults)
        else:
            print("\nKhông có sinh viên nào để tìm kiếm!")
    
    elif (key == 5):
        if(qlsv.soLuongSV() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showListSV(qlsv.getListSV())
            print("\nDanh sách sinh viên đã được sắp xếp theo điểm trung bình!")
        else:
            print("\nKhông có sinh viên nào để sắp xếp!")

    elif (key == 6):
        if(qlsv.soLuongSV() > 0):
            print("\n6. Sắp xếp sinh viên theo ngành")
            qlsv.sortByNganh()
            qlsv.showListSV(qlsv.getListSV())
            print("\nDanh sách sinh viên đã được sắp xếp theo ngành!")
        else:
            print("\nKhông có sinh viên nào để sắp xếp!")
    
    elif (key == 7):
        if(qlsv.soLuongSV() > 0):
            print("\n7. Hiển thị danh sách sinh viên")
            qlsv.showListSV(qlsv.getListSV())
        else:
            print("\nKhông có sinh viên nào để hiển thị!")

    elif (key == 0):
        print("\nBạn đã chọn thoát chương trình!")
        break
    else:
        print("\nLựa chọn không hợp lệ! Vui lòng chọn lại!")