work_time = float(input("Nhap so gio lam moi tuan: "))
salary = float(input("Nhap thu lao tren moi gio lam tieu chuan:"))
standard_time = 44
over_standard_time = max(0, work_time - standard_time)
salary_true = standard_time * salary + over_standard_time * salary*1.5
print(f"So tien thuc linh cua nhan vien: {salary_true}")