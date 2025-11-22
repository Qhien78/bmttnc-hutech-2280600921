from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("1. them sv")
    print("2. Cap nhat thong tin sinh vien boi ID")
    print("3. xoa sinh vien boi id")
    print("4. Tim kiem theo ten")
    print("5. Sap xep sinh vien theo diem tb")
    print("6. Sap xep theo ten")
    print("7. Hien thi danh sach")
    print("0. thoat")

    key = int(input("Nhap tuy chon: "))

    if key == 1:
        qlsv.nhapSinhVien()

    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            ID = int(input("Nhap Id: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach rong!")

    elif key == 3:
        ID = int(input("Nhap Id: "))
        if qlsv.deleleByID(ID):
            print("Da xoa.")
        else:
            print("Khong ton tai.")

    elif key == 4:
        keyword = input("Nhap ten: ")
        result = qlsv.findByName(keyword)
        qlsv.showSinhVien(result)

    elif key == 5:
        qlsv.sortByDiemTB()
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 6:
        qlsv.sortByName()
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 7:
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 0:
        break
