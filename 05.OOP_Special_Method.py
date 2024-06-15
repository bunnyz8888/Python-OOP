class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

    def __str__(self):
        return 'Day la {}, su dung {}'.format(self.ten, self.vu_khi)

    def __repr__(self):
        return 'ten: {}\nvu khi: {}\nmau sac: {}'.format(self.ten, self.vu_khi, self.mau_sac)


    def __len__(self):
        return len(self.ten)

    def __add__(self, mot_sieu_nhan_khac):
        return self.suc_manh + mot_sieu_nhan_khac.suc_manh

SN_A = SieuNhan('Sieu nhan Do', 'Kiem', 'Do')
SN_B = SieuNhan('Sieu nhan Xanh', 'Cung', 'Xanh')

print(SN_A)
print('%s' %SN_A)
print('%r' %SN_A)
print(len(SN_A))
print(SN_A + SN_B)
print(SieuNhan.__add__(SN_A, SN_B))
