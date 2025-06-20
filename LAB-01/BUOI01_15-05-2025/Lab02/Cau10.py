def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
# Sử dụng hàm và in kết quả
input_srting = input("Mời nhập chuỗi cần đảo ngược: ")
print("chuỗi đảo ngược là: ", dao_nguoc_chuoi(input_srting))