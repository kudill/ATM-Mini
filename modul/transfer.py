from database import database
from modul.cek_saldo import *

# Fungsi untuk transfer
def transfer(nomor_rekening):
    nomor_penerima = input("Masukkan nomor rekening penerima: ")
    nominal = int(input("Masukkan nominal (kelipatan 50000): "))
    if nominal % 50000 != 0 or nominal < 50000 or nominal > 1000000:
        print("Nominal tidak valid.")
        return

    konfirmasi = input(f"Konfirmasi transfer sebesar {nominal} ke {nomor_penerima}? (y/n): ")
    if konfirmasi.lower() != 'y':
        print("Transfer dibatalkan.")
        return

    print("==============================================")
    print("Transfer berhasil.")
    database[nomor_rekening]['saldo'] -= nominal
    print("Saldo terbaru:", cek_saldo(nomor_rekening))
    print("==============================================")
