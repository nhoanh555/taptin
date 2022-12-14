import os
from student import SinhVien
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, obj: SinhVien):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(obj, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print('Xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, tentaptin: str) -> SinhVien:
    try:
        with open(os.path.jion(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None


def main():
    path = 'O:\\k3'
    filename = 'sinhvien2.txt'
    sv1 = SinhVien('dau buoi', 2005, 10.0)
    ghi_sinhvien(path, filename, sv1)
    noidung = doc_sinhvien(path, filename)
    print(noidung)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()
