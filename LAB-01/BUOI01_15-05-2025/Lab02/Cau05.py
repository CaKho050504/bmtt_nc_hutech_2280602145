so_gio_lam = float(input("Nhập số giờ làm việc của NV: "))
luong_gio = float(input("Nhập mức lương tiêu chuẩn / giờ: "))

gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)

thuc_nhan = (gio_tieu_chuan*luong_gio + gio_vuot_chuan*luong_gio*1.5)

print("Mức lương thực nhận của NV: ",thuc_nhan)