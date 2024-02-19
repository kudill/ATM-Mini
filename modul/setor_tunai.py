from database import *
from modul.cek_saldo import *

# Fungsi untuk setor tunai
def setor_tunai(nomor_rekening):
    nominal = int(input("Masukkan nominal (kelipatan 50000): "))
    if nominal % 50000 != 0 or nominal < 50000 or nominal > 1000000:
        print("Nominal tidak valid.")
        return

    database[nomor_rekening]['saldo'] += nominal
    
    print("==============================================")
    print("Setor tunai berhasil.")
    print("Saldo terbaru:", cek_saldo(nomor_rekening))
    print("==============================================")
