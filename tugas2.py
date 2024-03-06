print('Program Python Menghitung Gaji Karyawan')

hari_kerja = 18
hari_kerja_perbulan = 20
gaji = 5000000
gaji_lembur = 500000

total_gaji = (hari_kerja / hari_kerja_perbulan) * (gaji + gaji_lembur)

format_total_gaji = f"Rp. {total_gaji:,.2f}"

print(f"Total gaji selama 18 hari/1 bulan (termasuk lembur): {format_total_gaji}")
