def tinhtongsochan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay:")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinhtongsochan(numbers)
print("Tong cac so chan trong list la: ", tong_chan)