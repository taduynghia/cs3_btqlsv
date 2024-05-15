class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        return f"MaKhoaHoc: {self.maKhoaHoc}, TenKhoaHoc: {self.tenKhoaHoc}, HinhThuc: {self.hinhThuc}, HocPhi: {self.hocPhi} VND"

    def __str__(self):
        return self.thongTinKhoaHoc()


class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHocDangKy = []

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHocDangKy.append(khoaHoc)

    def hienThiKhoaHoc(self):
        if not self.khoaHocDangKy:
            print(f"Học viên {self.tenHV} chưa đăng ký khóa học nào.")
        else:
            print(f"Học viên {self.tenHV} đã đăng ký các khóa học sau:")
            for khoaHoc in self.khoaHocDangKy:
                print(khoaHoc)

    def __str__(self):
        return f"MaHV: {self.maHV}, TenHV: {self.tenHV}, NgaySinh: {self.ngaySinh}"


# Tạo các đối tượng Khóa học
khoaHoc1 = KhoaHoc(1, "Lập trình Python", "Trực tuyến", 1500000)
khoaHoc2 = KhoaHoc(2, "Phân tích Dữ liệu", "Trực tiếp", 2500000)

# Tạo các đối tượng Học viên
hocVien1 = HocVien(1, "Nguyen Van A", "01/01/1990")
hocVien2 = HocVien(2, "Tran Thi B", "15/05/1992")

# Học viên đăng ký khóa học
hocVien1.dangKyKhoaHoc(khoaHoc1)
hocVien1.dangKyKhoaHoc(khoaHoc2)
hocVien2.dangKyKhoaHoc(khoaHoc2)

# Hiển thị thông tin khóa học đã đăng ký của học viên
hocVien1.hienThiKhoaHoc()
hocVien2.hienThiKhoaHoc()

# Hiển thị thông tin chi tiết của các khóa học
print(khoaHoc1.thongTinKhoaHoc())
print(khoaHoc2.thongTinKhoaHoc())
