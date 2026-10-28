# Pertemuan 13 — Debugging dan Testing

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Untirta  
**Kelas:** 3B  
**NIM:** 2225250177

## Kasus
Praktik ini menguji program Python untuk menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi. Program awal memiliki tiga bug logika yang diperiksa melalui test case.

## Test Case

| ID | Input | Expected | Actual Awal | Status Awal |
|---|---|---|---|---|
| T1 | Rata-rata `[80, 60, 90, 70]` | 75.0 | 60.0 | FAIL |
| T2 | Rata-rata `[100, 80]` | 90.0 | 36.0 | FAIL |
| T3 | Status nilai 60 | Lulus | Tidak lulus | FAIL |
| T4 | Status nilai 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | Nilai tertinggi `[80, 60, 90, 70]` | 90 | 0 | FAIL |

## Bug Report

### B01 — Perhitungan rata-rata
- **Gejala:** Hasil rata-rata tidak sesuai.
- **Test case:** T1 dan T2.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Jumlah nilai selalu dibagi 5, bukan jumlah data sebenarnya.
- **Perbaikan:** Membagi jumlah nilai dengan `len(nilai)`.

### B02 — Status kelulusan
- **Gejala:** Nilai 60 dinyatakan tidak lulus.
- **Test case:** T3.
- **Lokasi:** Fungsi `status()`.
- **Akar penyebab:** Kondisi menggunakan `nilai > 60`, sehingga nilai yang tepat 60 tidak lulus.
- **Perbaikan:** Mengubah kondisi menjadi `nilai >= 60`.

### B03 — Nilai tertinggi
- **Gejala:** Program menghasilkan nilai tertinggi 0.
- **Test case:** T5.
- **Lokasi:** Fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Program menggunakan operator `<`, sehingga nilai yang lebih besar tidak menggantikan nilai tertinggi sementara.
- **Perbaikan:** Menggunakan operator `>` dan memulai dari nilai pertama dalam daftar.

## Retest

Setelah perbaikan, program dijalankan kembali dengan hasil berikut.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| T1 | 75.0 | 75.0 | PASS |
| T2 | 90.0 | 90.0 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

## Cara Menjalankan

Jalankan program praktik melalui terminal VS Code:

`python praktik/praktik_4_debugging.py`

## Refleksi

Saya mempelajari bahwa program yang berhasil dijalankan belum tentu menghasilkan jawaban yang benar. Test case membantu menemukan kesalahan logika, sedangkan retest memastikan perbaikan bekerja sesuai harapan dan tidak menimbulkan kesalahan pada pengujian lain.