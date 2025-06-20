import os

from QLSV import QLSV

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

qlsv = QLSV()
while(True):
    clear_screen()
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN:")
    print("-------------------------------MENU-------------------------------")
    print("     1: Thêm sinh viên")
    print("     2: Cập nhật thông tin sinh viên theo ID")
    print("     3: Xóa sinh viên theo ID")
    print("     4: Tìm kiếm sinh viên theo tên")
    print("     5: Sắp xếp sinh viên theo điểm TB ")
    print("     6: Sắp xếp sinh viên theo tên chuyên ngành")
    print("     7: Hiển thị danh sách sinh viên")
    print("     0: Thoát chương trình!")
    key = int(input("Nhập lựa chọn: "))
    if (key == 1):
        qlsv.ThemSinhVien()
        print("Thêm sinh viên thành công!")
    elif (key == 2):
        ID = int(input("Nhập ID sinh viên cần cập nhật: "))
        qlsv.CapNhatSinhVien(ID)
        print("Cập nhật thông tin sinh viên thành công!")
    elif (key == 3):
        ID = int(input("Nhập ID sinh viên cần xóa: "))
        qlsv.XoaSinhVien(ID)
    elif (key == 4):
            name = input("Nhập tên sinh viên cần tìm kiếm: ")
            qlsv.TimKiemSinhVien(name)
            input()
    elif (key == 5):
            qlsv.SapXepSinhVienTheoDiemTB()
            input()
    elif (key == 6):
            qlsv.SapXepSinhVienTheoTenChuyenNganh()
            input()

    elif (key == 7):
        qlsv.HienThiDanhSachSV();
        input("Nhấn Enter để tiếp tục!")
    elif (key == 0):
        break
    else:
        print("Lựa chọn không hợp lệ!. Vui lòng chọn lại!")