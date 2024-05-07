class SinhVien:
    def __init__(self, maSV, tenSV, diemToan, diemVan, diemHoa):
        self.maSV = maSV
        self.tenSV = tenSV
        self.diemToan = diemToan
        self.diemVan = diemVan
        self.diemHoa = diemHoa

    def diem_trung_binh(self):
        return (self.diemToan + self.diemVan + self.diemHoa) / 3

    def __str__(self):
        return f"MaSV: {self.maSV}, TenSV: {self.tenSV}, DiemTB: {self.diem_trung_binh():.2f}"


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []

    def them_sinh_vien(self, sinh_vien):
        self.danh_sach_sv.append(sinh_vien)

    def in_sinh_vien_diem_tb_cao(self):
        print("Sinh viên có điểm trung bình lớn hơn 5:")
        for sv in self.danh_sach_sv:
            if sv.diem_trung_binh() > 5:
                print(sv)

    def in_sinh_vien_diem_hoa_thap(self):
        print("\nSinh viên có điểm hóa dưới 5:")
        for sv in self.danh_sach_sv:
            if sv.diemHoa < 5:
                print(f"MaSV: {sv.maSV}, TenSV: {sv.tenSV}, DiemHoa: {sv.diemHoa}")


# Tạo danh sách sinh viên
qlsv = QuanLySinhVien()
qlsv.them_sinh_vien(SinhVien(1, "An", 7, 5, 9))
qlsv.them_sinh_vien(SinhVien(2, "Binh", 3, 9, 4))
qlsv.them_sinh_vien(SinhVien(3, "Yen", 4, 6, 2))
qlsv.them_sinh_vien(SinhVien(4, "Minh", 5, 8, 7))
qlsv.them_sinh_vien(SinhVien(5, "Nghia", 10, 8, 9))

# In thông tin sinh viên theo yêu cầu
qlsv.in_sinh_vien_diem_tb_cao()
qlsv.in_sinh_vien_diem_hoa_thap()