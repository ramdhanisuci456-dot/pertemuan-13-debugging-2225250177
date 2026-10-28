def hitung_total(data):
    total = 0

    for nilai in data:
        total += nilai

    return total


def hitung_rata_rata(data):
    total = hitung_total(data)
    return total / len(data)


nilai_mahasiswa = [80, 90, 70]

hasil_total = hitung_total(nilai_mahasiswa)
hasil_rata_rata = hitung_rata_rata(nilai_mahasiswa)

print("Data nilai:", nilai_mahasiswa)
print("Total nilai:", hasil_total)
print("Rata-rata:", hasil_rata_rata)