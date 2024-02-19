from database import database
from modul.cek_saldo import *

# Fungsi untuk tarik tunai
def tarik_tunai(nomor_rekening):
    nominal = int(input("Masukkan nominal (kelipatan 50000): "))
    if nominal % 50000 != 0 or nominal < 50000 or nominal > 1000000:
        print("Nominal tidak valid.")
        return

    if nominal > 10000000:
        print("Nominal melebihi batas tarik tunai harian.")
        return

    konfirmasi = input(f"Konfirmasi tarik tunai sebesar {nominal}? (y/n): ")
    if konfirmasi.lower() != 'y':
        print("Tarik tunai dibatalkan.")
        return

    database[nomor_rekening]['saldo'] -= nominal
    print("==============================================")
    print("Tarik tunai berhasil.")
    print("Saldo terbaru:", cek_saldo(nomor_rekening))
    print("==============================================")
