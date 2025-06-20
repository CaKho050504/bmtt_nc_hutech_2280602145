lines = []

while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("Các dòng sau khi được chuyển thành chữ hoa: \n")
for line in lines:
    print(line.upper())