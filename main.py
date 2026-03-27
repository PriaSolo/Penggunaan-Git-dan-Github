from tabulate import tabulate
from kurs import data_kurs
import konverter

def tampilkan_tabel():
    print("\n=== KONVERTER MATA UANG ===")
    table_data = [[k, f"{v:,}"] for k, v in data_kurs.items()]
    print(tabulate(table_data, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_tabel()
    
    try:
        asal = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
        tujuan = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
        jumlah = float(input("Jumlah: "))

        jumlah_idr = konverter.konversi_ke_idr(jumlah, asal)
        hasil = konverter.konversi_dari_idr(jumlah_idr, tujuan)

        print(f"\n{asal} {jumlah:,.2f} = {tujuan} {hasil:,.2f}")
    except KeyError:
        print("Error: Kode mata uang tidak ditemukan!")
    except ValueError:
        print("Error: Masukkan angka yang valid untuk jumlah!")

if __name__ == "__main__":
    main()