from database import database

# Fungsi untuk memeriksa keberadaan rekening
def cek_rekening(nomor_rekening):
    return nomor_rekening in database

# Fungsi untuk memeriksa kebenaran PIN
def cek_pin(nomor_rekening, pin):
    return database[nomor_rekening]['pin'] == pin
