# studi_kasus_5_Celsines Rante Tasak


<img width="476" height="149" alt="Screenshot 2026-09-23 101159" src="https://github.com/user-attachments/assets/9a95acc7-9818-48e5-ab01-93d160d42191" />



<img width="490" height="400" alt="Screenshot 2026-09-23 101224" src="https://github.com/user-attachments/assets/af35529d-a115-47d3-8fa8-d7a16ecfe0ae" />


Penjelasan Singkat Kode Program
Program ini digunakan untuk menghitung biaya parkir kendaraan berdasarkan jenis kendaraan dan lama parkir.

def hitung_parkir(jenis, lama):
→ Membuat fungsi untuk menghitung biaya parkir.

if jenis == "mobil":
→ Mengecek apakah kendaraan adalah mobil. Jika iya, tarifnya Rp5.000/jam.

elif jenis == "motor":
→ Mengecek apakah kendaraan adalah motor. Tarifnya Rp3.000/jam.

total = tarif * lama
→ Menghitung total biaya dengan cara tarif dikali lama parkir.

return total
→ Mengembalikan hasil perhitungan biaya parkir.

input()
→ Digunakan untuk memasukkan data dari pengguna, yaitu jenis kendaraan, jam masuk, dan jam keluar.

int()
→ Mengubah input jam yang berupa teks menjadi angka.

lama_parkir = jam_keluar - jam_masuk
→ Menghitung berapa lama kendaraan parkir.

biaya = hitung_parkir(jenis, lama_parkir)
→ Memanggil fungsi untuk menghitung total biaya parkir.

print()
→ Menampilkan hasil data parkir dan total biaya ke layar.

