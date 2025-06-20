def dao_nguoc(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số nguyên cách nhau bởi dấu phẩy: \n")
numbers = list(map(int,input_list.split(',')))
print("Danh sách trước khi được đảo ngược: ",numbers)
print("\nDanh sách sau khi được đảo ngược: ",dao_nguoc(numbers))