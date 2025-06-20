from SinhVien import SinhVien

class QLSV:
    listSinhVien = []

    def TaoIDSinhVien(self):
        maxID = 0  
        if len(self.listSinhVien) > 0:
            maxID = max(sv._id for sv in self.listSinhVien)
        return maxID + 1


    def ThemSinhVien(self):
        svID = self.TaoIDSinhVien()
        name = input("Nhập tên sinh viên: ")
        sex = "null"
        while(sex == "null"):
            print("Sinh viên thuộc giới tính nào: \n")
            print("1: Nam       2: Nữ\n")
            luachongioitinh = input("Vui lòng chọn giới tính: ")
            if (luachongioitinh == "1"):
                sex = "Nam"
            if (luachongioitinh == "2"):
                sex = "Nữ"
        major = input("Nhập chuyên ngành sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.XepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)


    def XepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >=8):
            sv._hocLuc="Giỏi"
        elif (sv._diemTB >=6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >=5):
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"
        
    def CapNhatSinhVien(self, ID):
        ketQuaTimKiem = False
        if (self.listSinhVien.__len__() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    ketQuaTimKiem = True
                    name = input("Nhập tên sinh viên: ")
                    sex = "null"
                    while(sex == "null"):
                        print("Sinh viên thuộc giới tính nào: \n")
                        print("1: Nam       2: Nữ\n")
                        luachongioitinh = input("Vui lòng chọn giới tính: ")
                        if (luachongioitinh == "1"):
                            sex = "Nam"
                        if (luachongioitinh == "2"):
                            sex = "Nữ"
                    major = input("Nhập chuyên ngành sinh viên: ")
                    diemTB = float(input("Nhập điểm của sinh viên: "))
                    sv._name = name
                    sv._sex = sex
                    sv._major = major
                    sv._diemTB = diemTB
                    self.XepLoaiHocLuc(sv)
            if (ketQuaTimKiem == False):
                print("Không tìm thấy sinh viên có ID này!")
        else:
            print("Danh sách sinh viên hiện đang rổng! \nVui lòng thêm sinh viên trước khi thực hiện thao tác này!")

    def XoaSinhVien(self, ID):
        ketQuaTimKiem = False
        if (self.listSinhVien.__len__() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    ketQuaTimKiem = True
                    self.listSinhVien.remove(sv)
            if (ketQuaTimKiem == False):
                print("Không tìm thấy sinh viên có ID này!")
        else:
            print("Danh sách sinh viên hiện đang rổng! \nVui lòng thêm sinh viên trước khi thực hiện thao tác này!")

    def TimKiemSinhVien(self, name):
        ketQuaTimKiem = False
        if (self.listSinhVien.__len__() > 0):
            for sv in self.listSinhVien:
                if (sv._name.lower() == name.lower()):
                    ketQuaTimKiem = True
                    print("{:<8} {:<30} {:<8} {:<20} {:<8} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
            if (ketQuaTimKiem == False):
                print("Không tìm thấy sinh viên có tên này!")
        else:
            print("Danh sách sinh viên hiện đang rổng! \nVui lòng thêm sinh viên trước khi thực hiện thao tác này!")

    def SapXepSinhVienTheoDiemTB(self):
        if (self.listSinhVien.__len__() > 0):
            self.listSinhVien.sort(key=lambda sv: sv._diemTB, reverse=True)
            for sv in self.listSinhVien:
                print("{:<8} {:<30} {:<8} {:<20} {:<8} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        else:
            print("Danh sách sinh viên hiện đang rổng! \nVui lòng thêm sinh viên trước khi thực hiện thao tác này!")

    def SapXepSinhVienTheoTenChuyenNganh(self):
        if (self.listSinhVien.__len__() > 0):
            self.listSinhVien.sort(key=lambda sv: sv._major)
            for sv in self.listSinhVien:
                print("{:<8} {:<30} {:<8} {:<20} {:<8} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        else:
            print("Danh sách sinh viên hiện đang rổng! \nVui lòng thêm sinh viên trước khi thực hiện thao tác này!")

    def HienThiDanhSachSV(self):
        print("{:<8} {:<30} {:<8} {:<20} {:<8} {:<10}".format("ID","Họ tên","Giới","Ngành","ĐiểmTB","Học lực"))
        if (len(self.listSinhVien) > 0):
            for sv in self.listSinhVien:
                print("{:<8} {:<30} {:<8} {:<20} {:<8} {:<10}".format(sv._id,sv._name,sv._sex,sv._major,sv._diemTB,sv._hocLuc))


    