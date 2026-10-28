def baca_nilai(nama_file):
    nilai = []

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            nilai.append(float(baris.strip()))

    return nilai


try:
    data_nilai = baca_nilai("data_nilai.txt")
    print("Data nilai:", data_nilai)
except FileNotFoundError:
    print("File nilai tidak ditemukan.")
except ValueError:
    print("Ada data nilai yang bukan angka.")