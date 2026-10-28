def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [
    (75, "Lulus"),
    (60, "Lulus"),
    (59, "Tidak lulus"),
]

for nomor, (nilai, expected) in enumerate(test_case, start=1):
    actual = status_lulus(nilai)

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    print(f"T{nomor}: nilai={nilai}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print(f"Status:   {status}")
    print()