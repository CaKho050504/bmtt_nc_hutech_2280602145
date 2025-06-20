def tao_tuple(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số nguyên cách nhau bởi dấu phẩy: \n")
numbers = list(map(int,input_list.split(',')))
print("Danh sách bạn nhập từ bàn phím: ",numbers)
print("\nTuple từ danh sách bạn nhập: ",tao_tuple(numbers))