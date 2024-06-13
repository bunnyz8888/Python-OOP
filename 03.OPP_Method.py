class SieuNhan: #Class method
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @classmethod
    def from_string(cls, s): # thường những phương thức xử lí thế này hay có tên là from…
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)

    def cap_nhat_suc_manh(cls, smanh):
        cls.suc_manh = smanh

infor_str = "Sieu nhan do - Kiem - Do"
sieu_nhan_A = SieuNhan.from_string(infor_str)
sieu_nhan_A.cap_nhat_suc_manh(40)
print(sieu_nhan_A.__dict__)

''' Static method
class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @staticmethod
    def bien_hinh():
        print("1, 2, 3. Sieu nhan bien hinh")

sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")
sieu_nhan_A.bien_hinh()
'''