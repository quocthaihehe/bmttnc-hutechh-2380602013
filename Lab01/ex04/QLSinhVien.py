from SinhVien import SinhVien

class QLSinhVien:
    def __init__(self):
        self.listSV = []

    def generateID(self):
        maxID = 1 
        if (self.soLuongSV() > 0):
            maxID = self.listSV[0]._id
            for sv in self.listSV:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID += 1
        return maxID
    
    def soLuongSV(self):
        return len(self.listSV)
    
    def nhapSV(self):
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính (Nam/Nữ): ")
        major = input("Nhập ngành học: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSV.append(sv)

    def updateSV(self, ID):
        sv = self.findById(ID) # Sửa lỗi gọi sai tên hàm (cũ: findBySV)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính (Nam/Nữ): ")
            major = input("Nhập ngành học: ")
            diemTB = float(input("Nhập điểm trung bình: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại".format(ID))

    def sortByID(self):
        self.listSV.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSV.sort(key=lambda x: x._name, reverse=False)
        
    def sortByNganh(self):
        self.listSV.sort(key=lambda x: x._major, reverse=False)

    def sortByDiemTB(self):
        self.listSV.sort(key=lambda x: x._diemTB, reverse=True)
    
    def findById(self, ID):
        searchResult = None
        if(self.soLuongSV() > 0):
            for sv in self.listSV:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSV() > 0):
            for sv in self.listSV:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteID(self, ID):
        isDeleted = False
        sv = self.findById(ID)
        if(sv != None):
            self.listSV.remove(sv)
            isDeleted = True    
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
    
    def showListSV(self, listSV):
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format("ID", "Tên", "Giới tính", "Ngành học", "Điểm TB", "Học lực"))
        if(len(listSV) > 0):
            for sv in listSV:
               print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSV(self):
        return self.listSV