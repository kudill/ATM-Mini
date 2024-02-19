from modul.login import *
from modul.cek_saldo import *
from modul.setor_tunai import *
from modul.tarik_tunai import *
from modul.transfer import *

from database import database

import os

# bersihkan layar
def clear_screen():
    # Untuk Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Untuk sistem operasi lain (Linux/Mac)
    else:
        _ = os.system('clear')

# tampilan
def tampilkan_menu():
    print("________________")
    print("|     Menu:    |")
    print("|A. Cek Saldo  |")
    print("|B. Setor Tunai|")
    print("|C. Tarik Tunai|")
    print("|D. Transfer   |")
    print("|E. Logout     |")
    print("----------------")


def atm():
    clear_screen()
    print("===============================")
    print("||Selamat datang di BANK EMOK||")
    print("===============================")
    nomor_rekening = input("Masukkan nomor rekening: ")

    if not cek_rekening(nomor_rekening):
        print("Nomor rekening tidak valid.")
        return

    pin_attempt = 0
    while pin_attempt < 3:
        pin = input("Masukkan PIN: ")
        if cek_pin(nomor_rekening, pin):
            break
        else:
            pin_attempt += 1
            print("PIN salah. Kesempatan mencoba:", 3 - pin_attempt)

    if pin_attempt == 3:
        clear_screen()
        print("PIN salah 3 kali. Rekening diblokir.")
        return

    clear_screen()
    print("==================")
    print("||Login berhasil||")
    print("==================")
    print("Rekening atas nama: ", database[nomor_rekening]['nama'])
    print("======================================================")

    while True:
        tampilkan_menu()
        opsi = input("Pilih opsi (A/B/C/D/E): ").upper()

        if opsi == 'A':
            clear_screen()
            print("Saldo Anda:", cek_saldo(nomor_rekening))
            print("===========================")
        elif opsi == 'B':
            clear_screen()
            setor_tunai(nomor_rekening)
        elif opsi == 'C':
            clear_screen()
            tarik_tunai(nomor_rekening)
        elif opsi == 'D':
            clear_screen()
            transfer(nomor_rekening)
        elif opsi == 'E':
            clear_screen()
            print("Terima kasih. Anda berhasil logout.")
            break
        else:
            clear_screen()
            print("Opsi tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    atm()
