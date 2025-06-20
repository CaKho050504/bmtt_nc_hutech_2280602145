def tinh_tong_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong+=num
    return tong

input_list = input("Nhập danh sách các số nguyên cách nhau bởi dấu phẩy: \n")
numbers = list(map(int,input_list.split(',')))

print("Tổng các số chẵn có trong danh sách bạn vừa nhập là: ",tinh_tong_chan(numbers))