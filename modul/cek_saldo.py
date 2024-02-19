from database import database

# Fungsi untuk cek saldo
def cek_saldo(nomor_rekening):
    return database[nomor_rekening]['saldo']
