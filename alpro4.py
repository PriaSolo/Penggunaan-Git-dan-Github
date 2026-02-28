class umurError(Exception):
    def __init__(self, umur):
        self.umur = umur 
        super().__init__(f'umur {umur} tidak valid,harus diantara 17-60.')
def validasi_umur(umur):
    if umur < 17 or umur > 60:
        raise umurError(umur)
    return True
class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"Nama '{nama}' tidak valid, minimal harus 3 karakter.")

def validasi_nama(nama):
    if len(nama) < 3:
        raise NamaError(nama)
    return True

class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f"Nama terlalu pendek! Minimal 3 karakter.")

class umurError(Exception):
    def __init__(self, umur):
        self.umur = umur 
        super().__init__(f"Umur tidak memenuhi syarat (17-60 tahun).")

#vldasi
def validasi_nama(nama):
    if len(nama) < 3:
        raise NamaError(nama)
    return True

def validasi_umur(umur_str):
    if not umur_str.isdigit():
        raise ValueError("Umur harus berupa angka.")
    
    umur = int(umur_str)
    if umur < 17 or umur > 60:
        raise umurError(umur)
    return umur

def main():
    print("=== REGISTRASI PESERTA SEMINAR ===")
    
    nama_valid = ""
    umur_valid = 0
    email_valid = ""
    hp_valid = ""

    while True:
        try:
            nama_input = input("Nama lengkap: ")
            validasi_nama(nama_input)
            nama_valid = nama_input
            break
        except NamaError as e:
            print(f"[ERROR] {e}")

    while True:
        try:
            umur_input = input("Umur: ")
            umur_valid = validasi_umur(umur_input)
            break
        except (umurError, ValueError) as e:
            print(f"[ERROR] {e}")

    while True:
        try:
            email_input = input("Email: ")
            if "@" not in email_input:
                raise Exception("Email tidak valid, Harus mengandung '@'.")
            email_valid = email_input
            break
        except Exception as e:
            print(f"[ERROR] {e}")

    while True:
        try:
            hp_input = input("No HP: ")
            if not (hp_input.isdigit() and 10 <= len(hp_input) <= 13):
                raise Exception("No HP tidak valid! Harus 10-13 digit angka.")
            hp_valid = hp_input
            break
        except Exception as e:
            print(f"[ERROR] {e}")
        finally:
            print("Proses input selesai.")

    print("\n=== DATA PESERTA ===")
    print(f"Nama    : {nama_valid}")
    print(f"Umur    : {umur_valid} tahun")
    print(f"Email   : {email_valid}")
    print(f"No HP   : {hp_valid}")
    print("Status  : TERDAFTAR")
    
if __name__ == "__main__":
    main()