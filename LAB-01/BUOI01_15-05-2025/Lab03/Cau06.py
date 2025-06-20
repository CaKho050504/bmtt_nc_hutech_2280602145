def xoa_phan_tu(dic,key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False

my_dict = {'1': "Nguyễn Trường Giang",'2': "Phạm Tiến Đồng",'3': "Nguyễn Huỳnh Trúc Hiền" }
key_to_delete = '1'
result = xoa_phan_tu(my_dict,key_to_delete)
if result:
    print("Phần tử đã được xóa từ Dic: ",my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dic!")