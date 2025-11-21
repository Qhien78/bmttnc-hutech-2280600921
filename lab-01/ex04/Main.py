from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("1. them sv")
    print("2.Cap nhat thong tin sinh vien boi ID")
    print("3. xoa sinh vien boi id")
    print("4. Tim kim theo ten")
    print("5. Sap xep sinh vien theo diem tb")
    print("6. Sap xep theo chuyen nganh")
    print("7. Hien thi danh dach")
    print("0. thoat")
    
    key = int(input("Nhap tuy chon: "))
    if(key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\n Them thanh cong")
    elif(key ==2):
        if(qlsv.soluongSinhVien() >0):
            print("\n2. Cap nhat thong tin sinh vien.")
            print("\nNhap Id")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\n Danh Sach sinh vien trong!")
    elif(key ==3):
        if(qlsv.soLuongSinhVien() >0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap Id")
            ID = int(input())
            if(qlsv.deleleByID(ID)):
                print("\n Sinh vien co id = ", ID, "Da bi xoa")
            else:
                print("\n Sinh vien co id = ", ID, "khong ton tai")
    elif(key ==4):
        if(qlsv.soLuongSinhVien() >0):
            print("\n4.Tim kiem sinh vien theo ten.")
            print("\nNhap ten")
            name = int(input())
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\n Danh Sach sinh vien trong!")         
    elif(key ==5):
        if(qlsv.soLuongSinhVien() >0):
            print("\n5. Sap xep sinh vien theo gpa.")
            qlsv.sortByDiemTB(ID)
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh Sach sinh vien trong!")        
    elif(key ==6):
        if(qlsv.soLuongSinhVien() >0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName(ID)
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh Sach sinh vien trong!")
    elif(key ==7):
        if(qlsv.soLuongSinhVien() >0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\n Danh Sach sinh vien trong!")
    elif(key == 0):
        print("\nBan da thoat chuong trinh")
        break
    else:
        print("\nKhong co chuc nang nay")
        print("\nHay chon chuc nang trong menu")