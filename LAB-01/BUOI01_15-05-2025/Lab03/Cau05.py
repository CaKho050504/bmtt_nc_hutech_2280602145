def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_list = input("Nhập danh sách các số nguyên cách nhau bởi dấu phẩy: \n")
numbers = list(input_list.split(','))

print("Số lần xuất hiện của các phần tử:  ",dem_so_lan_xuat_hien(numbers))