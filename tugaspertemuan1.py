import math
import statistics

def main():
    mahasiswa_data = [
        {"nama": "Bagas", "nilai": 85},
        {"nama": "Andi", "nilai": 70},
        {"nama": "Siti", "nilai": 92},
        {"nama": "Budi", "nilai": 65},
        {"nama": "Dewi", "nilai": 78}
    ]
    
    daftar_nilai = []

    for mhs in mahasiswa_data:
        nama = mhs["nama"]
        nilai = mhs["nilai"]
        daftar_nilai.append(nilai)

        if nilai >= 80:
            status = "A"
        elif nilai >= 70:
            status = "B"
        else:
            status = "C"
            
        print(f"Mahasiswa: {nama} | Nilai: {nilai} | Status: {status}")

    print("-" * 40)

    rata_rata = statistics.mean(daftar_nilai)
    median_nilai = statistics.median(daftar_nilai)

    rata_rata_bulat = math.ceil(rata_rata)

    print(f"Rata-rata Nilai: {rata_rata_bulat}")
    print(f"Median Nilai: {median_nilai}")
    print(f"Nilai Tertinggi: {max(daftar_nilai)}")
    print(f"Nilai Terendah: {min(daftar_nilai)}")

main()