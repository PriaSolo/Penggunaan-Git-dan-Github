class Person:
    def __init__(self, nama, jenisKelamin, umur):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.umur = umur


class Karyawan(Person):
    def __init__(self, nama, jenisKelamin, umur, gaji):
        super().__init__(nama, jenisKelamin, umur)
        self.__gaji = gaji

    def get_gaji(self):
        return self.__gaji


class Rekening:
    def __init__(self, noRekening, PIN):
        self.noRekening = noRekening
        self.__PIN = PIN

    def get_PIN(self):
        return self.__PIN

    def set_PIN(self, PIN):
        if len(PIN) > 0:
            self.__PIN = PIN
        else:
            print("MASA LU LUPA PIN KOCAK")


objek1 = Person("owo owi selamanya", "MBG sehat", 67)
objek2 = Karyawan("nyawit ni orang", "sawit", 25, 7000000)
objek3 = Rekening("67676767", "indonesiasawit2045")

print(objek2.get_gaji())
print(objek3.get_PIN())
