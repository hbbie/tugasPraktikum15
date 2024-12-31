def validasi_input():
    """
    Fungsi untuk memvalidasi input data pendaftaran.

    Returns:
        bool: True jika semua input valid, False jika ada input yang tidak valid.
    """
    nama = input("Masukkan nama lengkap: ")
    if not nama.replace(" ", "").isalpha():
        print("Nama harus hanya berisi huruf dan spasi.")
        return False

    nomor_telepon = input("Masukkan nomor telepon: ")
    if not nomor_telepon.isdigit() or len(nomor_telepon) < 10:
        print("Nomor telepon harus hanya berisi angka dan minimal 10 digit.")
        return False

    email = input("Masukkan email: ")
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Email harus memiliki format yang benar, mengandung karakter '@' dan domain valid (misalnya, .com).")
        return False

    return True

if __name__ == "__main__":
    if validasi_input():
        print("Data pendaftaran valid.")
    else:
        print("Data pendaftaran tidak valid.")
