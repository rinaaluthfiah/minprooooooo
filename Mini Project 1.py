# Login Sederhana
while True:
    try:
        username = input("Masukkan Username anda: ")
        password = int(input("Masukkan Password anda: "))
        
        if username == 'Isrina Luthfiah' and password == 234568:
            print("Login berhasil!")
            break
        else:
            print("Username atau Password salah. Coba lagi.")
    except ValueError:
        print("Password harus berupa angka. Coba lagi.")

print("SELAMAT DATANG DI KALKULATOR INOY\n")

while True:
    try:
        jam_kerja = float(input("Jumlah Jam kerja: "))
        tarif_per_jam = float(input("Tarif per jam: "))
        
        gaji_dasar = jam_kerja * tarif_per_jam
        bonus = 0.1 * gaji_dasar if jam_kerja > 160 else 0
        total_gaji = gaji_dasar + bonus

        print(f"Gaji Dasar: {gaji_dasar}")
        print(f"Bonus: {bonus}")
        print(f"Total Gaji: {total_gaji}")

    except ValueError:
        print("Input tidak valid. Pastikan memasukkan angka.")
        continue

    ulang = input("Hitung gaji lagi? (ya/tidak): ").strip().lower()
    if ulang != 'ya':
        print("Terima kasih! Sampai jumpa.")
        break
